
##Question 1 dictonary ki help se har word ki frequancy check karna
# count={}
# name="ranjeet"
# for ch in name:
#     if ch not in count:
#         count[ch]=1
#     else:
#         count[ch]+=1
# print(count)

##Question 3  sabse badi value aur uski key find karna
# num={"a":5,"b":8,"c":78,"d":6}
# big_val=0
# big_key=None
# for i,v in num.items():
#     if v>big_val:
#         big_val=v
#         big_key=i
# print(big_val)#78

##question 4 check karna ki key exist karti hai yaa nai
# a={'name': 'ranjeet', 'age': 20, 'course': 'python', 'city': 'jaipur', 'mob': 9876543210}
# inputed=input("enter a key")
# if inputed in a:
#     print("key found")
# else:
#     print("key not found")

##Question 5 #2 dictonaries ko merge yaa add karna
# a={"name":"ranjeet","age":20}
# b= {"course":"python","city":"jaipur"}
# a.update(b)
# print(a)#{'name': 'ranjeet', 'age': 20, 'course': 'python', 'city': 'jaipur'}

##method 2
# a={"name":"ranjeet","age":20}
# b= {"course":"python","city":"jaipur"}
# c={"mob":9876543210}
# a.update(**b,**c)
# print(a)#{'name': 'ranjeet', 'age': 20, 'course': 'python', 'city': 'jaipur', 'mob': 9876543210}

##Method 3 #
# a={"name":"ranjeet","age":20}
# b= {"course":"python","city":"jaipur"}
# merge=a|b
# print(merge)#{'name': 'ranjeet', 'age': 20, 'course': 'python', 'city': 'jaipur'}

##question 6 values ka total nikala
# num={"a":1,"b":4,"c":3,"d":2}
# total=0
# for i in num.values():
#     total+=i
# print(total)

##Question 7 ak specif key ko find karna jisme user ke dwara input ki gyi value ho
# num={"a":1,"b":2,"c":3,"d":4}
# val=int(input("enter a value :"))
# result=[]
# for i,c in num.items():
#     if val==c:
#         result.append(i)
# print(result)

##Question 8 swap case
# intro={'name': 'ranjeet', 'age': 20, 'course': 'python', 'city': 'jaipur'}
# reve={}
# for i,c in intro.items():
#     i,c=c,i
#     reve[i]=c
# print(reve)

##Question 9 #2 dictonaries equal hai yaa nahi
# intro={'name': 'ranjeet', 'age': 20, 'course': 'python', 'city': 'jaipur'}
# intr={'name': 'ranjeet', 'age': 20, "city":"jaipur","course": "python"}
# if intro==intr:
#     print("equal")
# else:
#     print("not equal")

##Question 10 yaha short keys ke liye kiya gya hai
# num={"c": 1, "a": 3, "b": 2}
# result={}
# for i,c in sorted(num.items()):
#      result[i]=c
# print(result)

##Question 11 ak dictonary ko uski values ke basis par sort karna hai without keys ko use kiye

##Question 12 print karwana key aur values
# num={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7}
# for i,c in num.items():
#     print(i,c)

##Question 13 duplicate values remove karna
# num={"a":1,"b":2,"c":3,"d":1,"e":2,"f":6,"g":7,"h":7}
# new={}
# lis=[]
# for i,c in num.items():
#     if c not in lis:
#         lis.append(c)
#         new[i]=c
# print(lis)#[1, 2, 3, 6, 7]
# print(new)#{'a': 1, 'b': 2, 'c': 3, 'f': 6, 'g': 7}

##Question 14
# keys=["a","b","c","d","e","f"]
# values=[1,2,3,4,5,6]
# dic={}
# for i in range(len(keys)):
#     dic[keys[i]]=values[i]
# print(dic)

##Method 2
# keys=["a","b","c","d","e","f"]
# values=[1,2,3,4,5,6]
# dic=dict(keys,values))
# print(dic)#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

'''special note --> agar dono list mai se kisi bhi list mai elements kam yaa jyada hai toh dictonary small vali list ke according banegi aur un elements ko ignore kar degi jo extra hai list ke andar jisse key values sirf small wali dictonary ke according hi aayega'''
# keys=["a","b","c","d"]
# values=[1,2,3,4,5]
# dic=dict(keys,values))
# print(dic)#{'a': 1, 'b': 2, 'c': 3, 'd': 4}

##Question 15













##Question 22
# def m(**marks):
#     total=0
#     for i in marks.values():
#         total+=i
#     return total
# st=m(physic=90,maths=86,science=67)
# print(st)

##Question 23
# def g(**subjects):
#     total=0
#     for i in subjects.values():
#        total+=i
#     average= total/len(subjects)
#     return average
# student=g(physics=89,maths=87,science=56,hindi=48,sanskirit=78)
# print(student)

##Question 24
# def g(**subjects):
#     big=0
#     big_name=""
#     for m,i in subjects.items():
#         if big<i:
#           big=i
#           big_name=m
#     return (f'{big_name}: {big}')
# student=g(physics=89,maths=87,science=56,hindi=48,sanskirit=78)
# print(student) #physics: 89

##Question 25
# def g(**subjects):
#     big={}
#     for m,i in subjects.items():
#         if i>80:
#             big[m]=i
#     return big
# student=g(physics=89,maths=87,science=56,hindi=48,sanskirit=78)
# print(student)#{'physics': 89, 'maths': 87}

##question 26
# def g(**subjects):
#     failed=[]
#     for subject,marks in subjects.items():
#         if marks<33:
#           failed.append((subject,marks))
#     return failed
# student=g(physics=19,maths=87,science=56,hindi=28,sanskirit=78)
# print(student)#[('physics', 19), ('hindi', 28)]

##Question 27
# def g(**students):
#     for name, subjects in students.items():
#         failed = {}
#         for subject, marks in subjects.items():
#             if marks < 33:
#                 failed[subject] = marks

#         if len(failed) == len(subjects):
#             print(name, "-> Overall Fail")
#         elif len(failed) > 0:
#             print(name, "-> Fail in:", failed)
#         else:
#             print(name, "-> Pass")

# g(ravi={"physics": 89, "maths": 87, "hindi": 20},
#   amit={"physics": 10, "maths": 15, "hindi": 5},
#   sita={"physics": 80, "maths": 70, "hindi": 60},)


##Example 12
# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }
# for product in products.items():
#     print(product)#('Laptop', 990)('Smartphone', 600)('Tablet', 250)('Headphones', 70)

for i in range(1,100*100):
    print(".",end="")