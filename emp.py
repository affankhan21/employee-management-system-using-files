class Employee():
    def __init__(self,eid,ename,salary):
        self.eid=eid
        self.ename=ename
        self.salary=salary
    def __str__(self):
        return str(self.eid)+","+self.ename+","+str(self.salary)
       
    def display(self):
        print ("Eid = "+str(self.eid))
        print ("EName ="+self.ename)
        print ("salary ="+str(self.salary))
        
#e1=Employee(101,"affan",23000)          
#e1.display()