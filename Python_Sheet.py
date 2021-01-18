#-------------- print ----------------------

# a = 33
# f = 34.5
# name = 'alok'

# print('the numbers are {} and {} and the name is {}'.format(a ,f, name))
# print(f'the numbers are {a} ane {f} and the name is {name}')

#--------------- list operation ------------------

# list_1 = ['alok', 'abhi', 'tingu', 'ankul']

# list_1.insert(2,'car')
# list_1.append('bar')
# list_1.remove('car')
# list_1.pop(0)
# print(list_1)

# my_list = list(range(0,12))
# print(my_list)

# my_list = [i for i in range(0,15)]
# print(my_list)

# a = ['1','2','3'] + ['4','5','6']
# print(a)

# a = list(map(abs,[1,2,3,-4,-5,-6,-7]))
# print(a)

# --------------------Key word *not in*--------------------------
# list_1 = ['alok', 'abhi', 'tingu', 'ankul']
# name = str(input('enter a name'))
# if name not in list_1:
#      print('Bhaago bey')


# ------------------------ for loop ----------------------------

# names = ['alok', 'abhi', 'tingu', 'ankul', 'laddu', 'puchunki']

# for i in names[:3]:
#     print(i.title())


# --------------------------- dictionary -----------------

dict_1 = {'name': 'alok',
            'age' : '22'
            }
# print(dict_1.values())
# print(dict_1.keys())
# print(dict_1.items())
# print(dict_1.get('name'))
# dict_2 = dict_1.copy()
# print(dict_2)

# for key, value in dict_1.items():
#     print(key)
#     print(value)


# ------------------ justyfication -------------

# print('hello'.rjust(20,'-'))
# print('hello'.ljust(20,'-'))
# print('hello'.center(20,'-'))



#-------------Functions-------------

# def test():
#     print('kaisan ba badhiya to')

# def test(name):
#     print(f'kaisan ho {name} babuaaa')


# test('tingu')
# test('alok')


#-----------------explanation of LAMBDA FUNCTION-----------

# def test(x):
#     return x**2 + x*5 + 4

# print(test(-4))

# print((lambda x:x**2 + x*5 + 4)(-4))


# triple = lambda x:x*3
# add = lambda x: x+x

# print(triple(3))
# print(add(10))


#--------------------Explanation of MAP finction--------------

# def add_five(x):
#     return x+5
# nums = [11,12,13,14,15,16]
# result = list(map(add_five, nums))
# result = list(map(lambda x:x+5, nums))
# result = list(map(lambda x: x%2==0, nums))
# result = list(filter(lambda x: x%2==0, nums))

# print(result)

#----------------------Explanation for YIELD---------------------

# def countdown(x):
#     i = 0
#     while i<=x:
#         yield i
#         i+=1

# print(list(countdown(10)))

#-------------------Class---------------

# class Test():
#     def __init__(self, name):
#         self.name = name
#         self.title = 'Agrawal'                  # defualt
#         self.profession = 'pta nahi'
#     def print1(self):
#         print('He is',self.name, self.title)
    
#     def print2(self, pro):
#         self.profession = pro
#         print('His profession is ', pro)

# person1 = Test('alok')
# person2 = Test('abhi')
# person1.print1()
# person1.print2('software engineer')
# person2.print1()

#--------------any other key instead of self---------------
# recommended there should be self only
# class Test():
#     def __init__(alok, name, title):
#         alok.name = name
#         alok.title = title
    
#     def print1(alok):
#         print(alok.name)

# m = Test('a','b')
# m.print1()

#-----------------class child parent-----------------

# class Test():
#     def __init__(self, name):
#         self.name = name
#         self.title = 'Agrawal'                  # defualt
#         self.profession = 'pta nahi'
#     def print1(self):
#         print('He is',self.name, self.title)

# class Test2(Test):

#     def __init__(self,name):
#         super().__init__(name)
#         self.age = 80
#         self.wght = weight()
#         # self.age = 80             -------->>>>>> error
    
#     def print2(self):
#         print(self.age)
    
#     # def print2(self,a):             -------->>>>>> error
#     #     self.age =a
#     #     print(self.age)
# class weight():
#     def __init__(self, wajan = 70):
#         self.wajan = wajan    

#     def des(self):
#         print(self.wajan)
# m = Test2('alok')
# m.print1()
# m.print2()
# m.wght.des()
# w = weight(12054896748)
# w.des()


#-------------------Class with list-------------

# class ptanahi():
#     def __init__(self,list1):
#         # self.list1 = []
#         self.list1 = list1

#     def printlist(self):
#         print(self.list1)

#     def append_list(self, l):
#         self.list1.append(l)
# m = ptanahi(['a','b'])
# m.append_list('alok')
# m.printlist()

#------------File handaling------------

# commands--->
#                 touch 'filename'.txt    # to create any file
#                 cat 'filename'.txt      # to open and read that file  


# 'r' ---> open for reading(by default)
# 'w' ---> open for writing, truncating the first file
# 'x' ---> create new fiel and open it for writing
# 'a' ---> open for writing appending to the end of the file if it exists
# 'b' ---> binary mode
# 't' ---> text mode(default)
# '+' ---> open a disk file for updating(reading and writing)
# 'U' ---> Universal newline mode( deprecated)

# f = open('test.txt', 'r')
# print(f.read())
'----------------------------------------'
# f = open('test.txt', 'w')
# f.write('kya bauua sab bandhiyaa to........') #it takes exactly one argument 
# f.close()
# f = open('test.txt', 'r')
# print(f.read())

# '---------------------------------------------'

# with open('text.txt', 'w') as file:
#     file.write('hello \n hii \n bye bye')
# file.close()

# with open('text.txt', 'r') as f:
#     f = f.read()

# print(f.lstrip())


# '----------------------------------------------------------'

# file_path ='/home/alokagrwll/Files/Python/text.txt'

# with open(file_path, 'w') as file:
#     file.write('alok bhai zindabad zindabad.... \n bas bhai sab badhiya \n dekho ab kya hota h')

# file.close()

# with open(file_path, 'r') as f:
    # print(file.read())

#####################################
    
    # for i in file:
    #     print(i)

##########################################
#     line = f.readlines()

# string = ''

# for i in line:
#     string += i.rstrip()

# print(string) 1


#---------------------------------- AGRV -----------------------

# from sys import argv

# script, para = argv

# print(f'pta nahi kya hone wala hai {para}')

# # for run in command shell $ python3 file_name agrv
                         # $ python3 prac.py kuchbhi

#-----------------------------------itertools---------------------

'''from itertools import count

for i in count(3):
    print(i)
    if i>50:
        break'''

# from itertools import accumulate, takewhile, product

# nums = list(accumulate(range(8)))
# print(nums)  # [0,<-difference of 0-> 1,<-2-> 3,<-3-> 6,<-4-> 10,<-5-> 15,<-6-> 21,<-7-> 28]

# nums_takewhile = list(takewhile(lambda x: x<=6, nums))
# print(nums_takewhile)

# l = ['a','b']
# print(list(product(l ,range(3))))

#------------------Try Exception-----------------

# print('please enter any two numbers')

# a=int(input())
# b=int(input())

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('bhag bey')


#--------------------------------------------------------
# print('enter file name')
# filename = input('>')
# try:
#     with open(filename, 'r') as file:
#         print(file.read())

# except FileNotFoundError:
#     print('file doesnt exist')


#----------------------JSON-----------------------------

# import json

# num = [1,2,3,4,5,6,7] 

# filename = 'test.json'

# with open(filename, 'w') as file:
#     json.dump(num,file)

# file.close()

# with open(filename, 'r') as f:
#     print(f.read())


# with open(filename) as file:
#     my_list = json.load(file)

# print(my_list, 'badhiya')

#---------------------------------------------------------------

# import json
# import sys

# name = sys.argv[1]

# try:
#     with open(name, 'r') as file:
#         p = json.load(file)
#     print(p)

# except:
#     with open(name, 'w') as file:
#         print('what do you want to wrtie')
#         wrt = input()
#         file.write(wrt)
#     file.close()

# with open(name) as f:
#     p = json.loads(f)
#     print(p)
# with open(name, 'w') as file:
#         print('what do you want to wrtie')
#         wrt = input()
#         file.write(wrt)
#         file.close()


#----------------------ASSERT keyword--------------------

# passw = input('enter your pass')

# assert passw == 'admin' , 'entered wrong password'


#-----------------------------------------------------------    
# s='12:45:00PM'

# if s[-2:] == 'AM' and s[:2] == '12':
#         hr = '00'
#         print(hr+s[2:-2])

# elif s[-2:] == 'AM' :
#     print(s[:-2])

# elif s[-2:] == 'PM' and s[:2] == '12':
#     print(s[:-2])

# else:
#         hr = s[:2]
#         mn = s[3:5]   
#         ss = s[6:8]

#         hr = int(hr) + 12
    
#         print((str(hr)+":"+mn+":"+ss))
