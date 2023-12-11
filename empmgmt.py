
from emp import Employee
class Empmgmt():
    def addEmp(self):
        eid=int(input("ENTER THE ID OF EMPLOYEES       :"))
        ename=input("ENTER THE NAME OF EMPLOYEE        :")
        salary=int(input("ENTER THE SALARY OF EMPLOYEE :"))  
        e1=Employee(eid,ename,salary)
        with open("data1.txt","a") as fp:
                fp.write(str(e1)+"\n")

    def displayDetails(self):
        with open("data1.txt","r") as fp:
                for e in fp:
                   list1=e.split(",")
                   print("-----------EMPLOYEE DETAIL---------------------")
                   print("EMPLOYEE ID     IS  :",list1[0])
                   print("EMPLOYEE NAME   IS  :",list1[1])
                   print("EMPLOYEE SALARY IS  :",list1[2])
                   print("------------------------------------------------")
             
    def searchEmp(self,eid):
          with open("data1.txt","r") as fp:
                for e in fp:
                    try:
                        e.index(str(eid),0,4)
                        print("-----------------------------------------------")
                        print("EMPLOYEE FOUND")
                        list2=e.split(",")
                        print("-----------EMPLOYEE DETAIL---------------------")
                        print("EMPLOYEE ID     IS  :",list2[0])
                        print("EMPLOYEE NAME   IS  :",list2[1])
                        print("EMPLOYEE SALARY IS  :",list2[2])
                        print("-----------------------------------------------")
                        break
                        

                    except ValueError:
                        pass
                else:
                    print("EMPLOYEE NOT FOUND")
    def  deleteEmp(self,eid):
        container=[]
        flag=False
        with open("data1.txt","r") as fp:
            for e in fp:
                list2=e.split(",")
                if(list2[0]==str(eid)):
                    flag=True
                    print("EMPLOYEE DELETED SUCCESFULLY")
                    
                else:
                    container.append(e)
                    
            if(flag==True):
                with open("data1.txt","w") as fp:
                    for x in container:
                        fp.write(x)

      

    def update(self, id):
        container = []
        found = False
        with open("data1.txt","r") as fp:
            for e in fp:
                sep_list = e.split(",")
                if(sep_list[0] == str(id)):
                    found =True
                    ans = input("Do you want to change name: (y/n)")
                    if(ans =='y'):
                        sep_list[1] = input("Enter new name:")
                    ans = input("Do you want to change salary: (y/n)")
                    if(ans =='y'):
                        sep_list[2] = input("Enter new salary:")
                    
                    e = ','.join(sep_list)
                
                container.append(e)
        if(found ==True):
            with open("data1.txt", 'w') as fp:
                for x in container:
                    fp.write(x)
        else:
            print("Id not present")

        
