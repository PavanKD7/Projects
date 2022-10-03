
#SIMPLE PROJECT ON RAILWAY RESERVATION



class Railway_reservation:
    def __init__(self,train_name,train_no,Class) :
        self.train_name=train_name
        self.train_no=train_no
        
        self.Class=Class
        self.fare=0
        
        self.seats=0   
    def Seats_availability(self):
        
        if(self.Class=="SL"):
            self.seats=150
            return self.seats

        elif (self.Class=="AC_3Tier"):
            self.seats=70
            return self.seats
            
        elif (self.Class=="AC_2Tier"):
            self.seats=2
            return self.seats
            
        elif (self.Class=="AC_1Tier"):
            self.seats=10
            return self.seats
            
    def Fare(self):
        if(self.Class=="SL"):
            self.fare=290
            return self.fare

        elif (self.Class=="AC_3Tier"):
            self.fare=750
            return self.fare
            
        elif (self.Class=="AC_2Tier"):
            self.fare=1450
            return self.fare
            
        elif (self.Class=="AC_1Tier"):
            self.fare=2500
            return self.fare
        
    def availability(self):
        print("--------------------------------------------------------------------------")
        print(f"name of the train is :{self.train_name} and train Number is:{self.train_no}")
        print(f"Class is: {self.Class} and fare of the class is: {self.fare}")
        print(f"the number of seats available in the train is: {self.seats}")
        print("--------------------------------------------------------------------------")

    def book_ticket(self):
        if (self.seats>0):
            print(f"your ticket has been booked! and your seat number is :{self.seats}")
        
        else:
            print("OOPS!! No seats available in the train, WAITING LIST REGRET")
        self.seats=self.seats-1
        
train_name=input("enter train name:")
Class=input("enter the class:")
t=Railway_reservation(train_name, 15985 ,Class)

t.Seats_availability()
t.Fare()
t.availability()

t.book_ticket()
t.book_ticket()
t.book_ticket()
t.book_ticket()
t.book_ticket()


print("----------------------------HAPPY JOURNEY------------------------------------------")

    


        
