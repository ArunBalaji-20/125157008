from flask import Flask
import requests
app=Flask(__name__)


#token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIxMTM1MzgyLCJpYXQiOjE3MjExMzUwODIsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjA3MzdkOGM0LThiZGMtNGU2Yi04NmI2LWMyOWRkNmMzOTBjNCIsInN1YiI6IjEyNTE1NzAwOEBzYXN0cmEuYWMuaW4ifSwiY29tcGFueU5hbWUiOiJjb21wYW55YXJ1biIsImNsaWVudElEIjoiMDczN2Q4YzQtOGJkYy00ZTZiLTg2YjYtYzI5ZGQ2YzM5MGM0IiwiY2xpZW50U2VjcmV0Ijoid3daTW1EdldhS0Jwb3J0UiIsIm93bmVyTmFtZSI6IkFydW4gQmFsYWppIEIiLCJvd25lckVtYWlsIjoiMTI1MTU3MDA4QHNhc3RyYS5hYy5pbiIsInJvbGxObyI6IjEyNTE1NzAwOCJ9.E159Uq-rFvMbpPDn2_V9hqGZLuQWG3D2Bp1KsHAjFss
data={}
data['numbers']=[]
data['windowPrevstate']=[]
data['windowCurrState']=[]
data['avg']=0

#url 
url = 'http://20.244.56.144/test/'
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIxMTQyMDg4LCJpYXQiOjE3MjExNDE3ODgsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjA3MzdkOGM0LThiZGMtNGU2Yi04NmI2LWMyOWRkNmMzOTBjNCIsInN1YiI6IjEyNTE1NzAwOEBzYXN0cmEuYWMuaW4ifSwiY29tcGFueU5hbWUiOiJjb21wYW55YXJ1biIsImNsaWVudElEIjoiMDczN2Q4YzQtOGJkYy00ZTZiLTg2YjYtYzI5ZGQ2YzM5MGM0IiwiY2xpZW50U2VjcmV0Ijoid3daTW1EdldhS0Jwb3J0UiIsIm93bmVyTmFtZSI6IkFydW4gQmFsYWppIEIiLCJvd25lckVtYWlsIjoiMTI1MTU3MDA4QHNhc3RyYS5hYy5pbiIsInJvbGxObyI6IjEyNTE1NzAwOCJ9.xdD2RRQYd28zCwUhDk5zzxb2JjeTe38MeadxW20QOiY'

headers= {'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}


def average(nums):
    total=0
    size=len(nums)
    for i in nums:
        total=total+i
    avg=total/size
    return avg



@app.route('/')
def home():
    return render_template_string('hi')

@app.route('/gettoken')
def get_token():
    url2='http://20.244.56.144/test/auth'
    data2={'companyName': 'companyarun', 'clientID': '0737d8c4-8bdc-4e6b-86b6-c29dd6c390c4', 'clientSecret': 'wwZMmDvWaKBportR', 'ownerName': 'Arun Balaji B', 'ownerEmail': '125157008@sastra.ac.in', 'rollNo': '125157008'}

    response = requests.post(url2, json=data2)
    res_data=response.json()
    token=res_data.get('access_token',None)

    return f'{token}'

@app.route('/numbers/e')
def even():
    
    urle=url+'even'
    #print(urle)
    res=requests.get(url=urle,headers=headers)
    if res.status_code!=200:
        
        return 'Invalid token'
    response_data=(res.json())
  

    print(response_data,'response')
    data['numbers']=response_data.get('numbers',None)
    if len(data['windowPrevstate'])==0:
        data['windowCurrState']=response_data.get('numbers',None)
        #print(data)
        avg=average((data['numbers']))
        data['avg']=avg

        temp=data.copy()
        data['windowPrevstate']=data['numbers']
        print(data,'first response')
        return temp

    else:
        currstate=data['numbers']
        prevstate=data['windowPrevstate']
        if len(currstate)>10:
            for i in currstate:
                if i in prevstate:
                    currstate.remove(i)
            data['windowCurrState']=currstate[:10]
            avg=average((data['numbers']))
            data['avg']=avg
            temp=data.copy()
            data['windowPrevstate']=data['windowCurrState']
            print(data,'2nd response')
            return temp
        

        


@app.route('/numbers/p')
def primes():
    urle=url+'primes'
    #print(urle)
    res=requests.get(url=urle,headers=headers)
    if res.status_code!=200:
        return 'Invalid token'
    response_data=(res.json())
    print(response_data,'response')
    data['numbers']=response_data.get('numbers',None)
    if len(data['windowPrevstate'])==0:
        data['windowCurrState']=response_data.get('numbers',None)
        #print(data)
        avg=average((data['numbers']))
        data['avg']=avg

        temp=data.copy()
        data['windowPrevstate']=data['numbers']
        print(data,'first response')
        return temp

    else:
        currstate=data['numbers']
        prevstate=data['windowPrevstate']
        if len(currstate)>10:
            for i in currstate:
                if i in prevstate:
                    currstate.remove(i)
            data['windowCurrState']=currstate[:10]
            avg=average((data['numbers']))
            data['avg']=avg
            temp=data.copy()
            data['windowPrevstate']=data['windowCurrState']
            print(data,'2nd response')
            return temp
        


@app.route('/numbers/f')
def fibo():
    
    urle=url+'fibo'
    #print(urle)
    res=requests.get(url=urle,headers=headers)
    if res.status_code!=200:
        
        return 'Invalid token'
    response_data=(res.json())
    print(response_data,'response')
    data['numbers']=response_data.get('numbers',None)
    if len(data['windowPrevstate'])==0:
        data['windowCurrState']=response_data.get('numbers',None)
        #print(data)
        avg=average((data['numbers']))
        data['avg']=avg

        temp=data.copy()
        data['windowPrevstate']=data['numbers']
        print(data,'first response')
        return temp

    else:
        currstate=data['numbers']
        prevstate=data['windowPrevstate']
        if len(currstate)>10:
            for i in currstate:
                if i in prevstate:
                    currstate.remove(i)
            data['windowCurrState']=currstate[:10]
            avg=average((data['numbers']))
            data['avg']=avg
            temp=data.copy()
            data['windowPrevstate']=data['windowCurrState']
            print(data,'2nd response')
            return temp
        


@app.route('/numbers/r')
def random():
    
    urle=url+'rand'
    #print(urle)
    res=requests.get(url=urle,headers=headers)
    if res.status_code!=200:
        
        return 'Invalid token'
    response_data=(res.json())
    print(response_data,'response')
    data['numbers']=response_data.get('numbers',None)
    if len(data['windowPrevstate'])==0:
        data['windowCurrState']=response_data.get('numbers',None)
        #print(data)
        avg=average((data['numbers']))
        data['avg']=avg

        temp=data.copy()
        data['windowPrevstate']=data['numbers']
        print(data,'first response')
        return temp

    else:
        currstate=data['numbers']
        prevstate=data['windowPrevstate']
        if len(currstate)>10:
            for i in currstate:
                if i in prevstate:
                    currstate.remove(i)
            data['windowCurrState']=currstate[:10]
            avg=average((data['numbers']))
            data['avg']=avg
            temp=data.copy()
            data['windowPrevstate']=data['windowCurrState']
            print(data,'2nd response')
            return temp

    

    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9876)