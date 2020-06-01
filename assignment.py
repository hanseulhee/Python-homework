class LikeLion:
    def __init__(self,name,phone,gender):
        self.name = name
        self.phone = phone
        self.gender = gender
        
    def intro(self):
        print("이름은 %s이고 전화번호는 %s이고 성별은 %s입니다."%(self.name,self.phone,self.gender))

person_list=[]
while True:
    name=input("이름을 입력하세요 : ")
    if name == "그만":
        name=name
        for x in person_list:
            x.intro()
        break

    phone=input("전화번호를 입력하세요 : ")
    gender=input("성별을 입력하세요(male이나 female로 작성해주세요) : ")

    if gender == "male" or gender == "female":        
        gender=gender
    else: 
        gender="unknown"

  
    person = LikeLion(name,phone,gender)
    person_list.append(person)
    for x in person_list:
        x.intro()
       
        


    
    









    
       