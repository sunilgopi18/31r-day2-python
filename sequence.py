#numeric:int,float,complex,boolean
#sequence:list,tuple,string,range
#Complex Numbers:
comp1=6+9j
comp2=9-5j
print(comp1+comp2)
print(comp1-comp2)
print(comp1*comp2)
print(comp1**comp2)
#print(comp1%comp2)    #it cannot suport on complex number
#print(comp1//comp2) #it cannot suport on complex number
print(comp1/comp2)

#Boolean -True/False
bool1=2
bool2=3
print(2>=3)
print(2<3)
print(2<=3)
bool=True
print(type(bool))


#Sequence:list,tuple,string,range
list1 =[1,2,3,4,[10,29,39],'sunil'] #creating a list 
print(list1) # here printing a list 
print(list1[3]) # here using index printing the output
print(list1[-1]) # here using negative index printing the last data of list
print(type(list1)) # here finding  a  what type of data
print(list1[1:]) #  here using slicing printing the output from data
print(list1[0::]) #  here using slicing printing the output from data
print(list1[::]) #  here using slicing printing the output from data
print(list1[:4]) #  here using slicing printing the output from data
print(list1[1:4]) #  here using slicing printing the output from data
print(list1[4][1]) #  here using slicing printing the output from data
print(list1[5]) #  here using slicing printing the output from data
print(list1[-1:-5:-1])

#tuple
t1=(1,2,3,'sunil',4,5,6)
print(t1)
print(t1[2])
print(t1[1:])
print(t1[1::])
print(type(t1))
print(t1[-1])
print(t1[0::])
print(t1[::5])
print(t1[-1:-5:-1])
#range
print(list(range(0,100)))# it print 0 t0 99
print(list(range(100,-0))) #it gives empty list
print(list(range(100,0,-1))) # it print 100 to 1 
