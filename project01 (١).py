#----------------------------------------------------------------------#
class stack():
    def __init__(self,list):
        self.list=list
        self.top=-1

    def push(self):
        a=input("Enter the element:")
        if a.isnumeric():
            self.list.append(int(a))
            return int(a)
        else:
            print("....................\n", "pleas enter number\n", "....................")
            return None
    def pop(self):
        if len(self.list)!=0:
            self.list.pop()
        else:
            print("------------------------\n","THE LIST IS EMPTY\n","-----------------------")
    def operation(self):
        global top
        self.top = len(self.list) - 1
        while True:
            print("\n", self.list, " TOP==> ", self.TOP())
            op = input("CHoose number of Operation\n"
                       "1-ADD ELEMENT.\n"
                       "2-DELETE ELEMENT.\n"
                       "3-Back.\n==> ")
            if op == "1":
                if self.push() !=None:
                    self.top += 1
            elif op == "2":
                self.pop()
                if self.top!=-1:
                    self.top -= 1
            elif op == "3":
                break
            else:
                print("*********************\n","*** Wrong enter ,pleas choose number of acess ***\n","*****************")
    def TOP(self):
        return self.top

#-----------------------------------------------------------#
class queue():
    def __init__(self,list):
        self.list=list
        self.front=-1
        self.rear=-1
    def en_Q(self):
        a = input("enter the element")
        if a.isnumeric():
            self.list.append(int(a))
            return int(a)
        else:
            print("....................\n", "pleas enter number\n", "....................")
            return None
    def de_Q(self):
        if len(self.list)>0:
            self.list.pop(0)
        else:
            print("***************\n","THE LIST IS EMPTY\n","***************************")

    def Operation(self):
        global rear,front
        if len(self.list)>0:
            self.front=0
        else:
            if self.front!=-1:
                self.front=-1
        if self.rear!=-1:
            self.rear=len(self.list)-1
        while True:
            print("\n", self.list, " REAR==> ", self.Rear(), "FRONT==>", self.front)
            op = input("CHoose number of Operation :\n"
                       "1-ADD ELEMENT.\n"
                       "2-DELETE ELEMENT.\n"
                       "3-Back.\n==> ")
            if op == "1":
                if queue.en_Q(self ) !=None:
                    self.front = 0
                    self.rear += 1
            elif op == "2":
                if self.front == self.rear:
                    queue.de_Q(self)
                    if self.front!=-1 and self.rear!=-1:
                        self.rear -= 1
                        self.front -= 1
                else:
                    queue.de_Q(self)
                    self.rear -= 1
            elif op == "3":
                break
            else:
                print("------------------------------\n","*** Wrong enter ,pleas choose number of acess ***\n","-------------------------")
    def Rear(self):
        return self.rear
    def Front(self):
        return self.front
#-------------------------------------------------------------------------#
class de_que():
    def __init__(self,list):
        self.list=list
        self.front=self.rear=-1
    def en_deqright(self):
        a = input("enter the element")
        if a.isnumeric():
            self.list.append(int(a))
            return int(a)
        else:
            print("....................\n", "pleas enter number\n", "....................")
            return None
    def en_deqlift(self,):
        ele = input("enter element")
        if ele.isnumeric():
            self.list.insert(0,int(ele))
            return int(ele)
        else:
            print("....................\n","pleas enter number\n","....................")
            return None

    def de_deqright(self):
        if len(self.list)>0:
            self.list.pop()
        else:
            print("THE LIST IS EMPTY,Try again\n")
    def de_deqlift(self):
        if len(self.list)>0:
            self.list.pop(0)
        else:
            print("THE LIST IS EMPTY,Try again")

    def OPeration(self):
        global rear,front
        if len(self.list)>0:
            self.front=0
        else:
            if self.front!=-1:
                self.front=-1
        self.rear=len(self.list)-1
        while True:
            print("\n", self.list, " REAR==> ", self.Rear(), "FRONT==>", self.front)
            op = input("CHoose number of Operation\n"
                       "1-ADD ELEMENT TO RIGHT.\n"
                       "2-ADD ELEMENT TO LEFT.\n"
                       "3-DELETE ELEMENT FROM RIGHT.\n"
                       "4-DELETE ELEMENT FROM LEFT.\n"
                       "5-Back.\n==> ")
            if op == "1":
                if self.en_deqright()!=None:
                    self.front = 0
                    self.rear += 1
            elif op == "2":
                if self.en_deqlift( )!=None:
                    self.front = 0
                    self.rear += 1
            elif op == "3":
                if self.front == self.rear:
                    de_que.de_deqright(self)
                    if self.rear!=-1 and self.front!=-1:
                        self.rear -= 1
                        self.front -= 1
                else:
                    de_que.de_deqright(self)
                    if self.rear!=-1:
                        self.rear -= 1
            elif op == "4":
                if self.front == self.rear:
                    de_que.de_deqlift(self)
                    if self.front!=-1 and self.rear!=-1:
                        self.rear -= 1
                        self.front -= 1
                else:
                    de_que.de_deqlift(self)
                    if self.rear!=-1:
                        self.rear -= 1
            elif op == "5":
                break
            else:
                print("*** Wrong enter ,pleas choose number of acess ***")
    def Rear(self):
        return self.rear
    def Front(self):
        return self.front

#----------------------------------------------------------------------------#
#
class access():
    def __init__(self):
        self.list=[]

    def process(self):
        print(""""
           *************************************
           *************************************
           **                                 **
           **                                 **
           **    ///////////////////////////  **
           **   // WELCOM TO THE PROGRAM //   **
           **  ///////////////////////////    **
           **                                 **
           **                                 **
           *************************************
           *************************************
        """)
        while True:
            key=input(""""
           ####################################################
           ####################################################
           ##                                                ##
           ##      ///////////////////////////////////       ##
           ##     // CHOOSE NUMBER TO ACCESS WAYS  //        ##
           ##    ///////////////////////////////////         ##
           ##                                                ##
           ##               (1),(2),(3),(4)                  ##
           ##             CHOOSE (1) TO  Stack               ##
           ##             CHOOSE (2) TO  Queue               ##
           ##             CHOOSE (3) TO  Deque               ##
           ##             CHOOSE (4) TO  Stop program        ##
           ##                                                ##
           ####################################################
           ####################################################
           ENTER NUMBER ==>  """)
            if key=="1":
                oop=stack(self.list)
                oop.operation()
                print("\n",self.list," TOP==> ",oop.TOP(),"\n")
            elif key=="2":
                oop1=queue(self.list)
                oop1.Operation()
                print("\n",self.list, " REAR==> ",oop1.Rear() ,"FRONT==>",oop1.front ,"\n")
            elif key=="3":
                oop2=de_que(self.list)
                oop2.OPeration()
                print("\n",self.list, " REAR==> ",oop2.Rear() ,"FRONT==>",oop2.Front() ,"\n")
            elif key=="4":
                print("""
                -----------------------------------
               |  THANK YOU FOR USING THE PROGRAM  |
                -----------------------------------
                """)
                break
            else:
                print("\n","WRONG ENTER ?!!","\n")


a=access()
a.process()

