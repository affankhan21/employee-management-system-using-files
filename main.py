from empmgmt import Empmgmt
if(__name__=="__main__"):
    obj=Empmgmt()
 
    choice = 0
    while choice != 6:
        print("\t\t1.ADD NEW EMPLOYEE")
        print("\t\t2.DISPLAY THE DETAILS")
        print("\t\t3.SEARCH AN EMPLOYEE")
        print("\t\t4.DELETE  AN EMPLOYEE")
        print("\t\t5.UPDATE  AN EMPLOYEE")
        print("\t\t6.EXIT")
        choice=int(input("ENTER THE CHOICE :"))
        if (choice==1):
            obj.addEmp()
            
        elif(choice==2):
            obj.displayDetails()
        elif (choice==3): 
            eid=int(input("ENTER EMPLOYEE TO SEARCH :"))
            obj.searchEmp(eid)   
        elif (choice==4): 
            eid=int(input("ENTER EMPLOYEE TO SEARCH :"))
            obj.deleteEmp(eid)  
        elif(choice == 5):
            id = int(input("Enter id to Update: "))
            obj.update(id)
        else:
            pass
