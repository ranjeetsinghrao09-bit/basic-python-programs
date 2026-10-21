##Example 1
# print("python"[::-2].upper()) #NHY

##Example 2
# print("Hello World".swapcase().istitle())

##Example 3
# print("one two three".split(" ")) #['one', 'two','three']

##Example 4
# print(len("one two three".split(" ")),len("one two three".split())) #33

##Example 5
# print("a\nb\nc".splitlines())#["a","b","c"]

##Example 6
# print("Straße".lower()=="STRASSE".casefold()) #False

##Example 7
# print("Straße".lower()=="strase".casefold()) #False

##Example 8
# print("Straße".upper()=="STRASSE".casefold()) #False

##Example 9
# print("Straße".casefold()=="STRASSE".casefold()) #True

##Example 10
# print("abcabc".find("c",3,5)) #-1

##Example 11
# print("abc".find("d")+"abc".count("d")) #-1

##Example 12
# print(" data ".strip().capitalize().ljust(6,"-").rjust(8,"*")) #**DATA--

##Example 13
# s="hello"
# print(s.upper(),s) #HELLO hello

##Example 14
# print("abc".index("d")) #Value Error

##Example 15
# print("python".removeprefix("py").removesuffix("on").upper())#TH

##Example 16
# print("abc".isalpha()+"123".isdigit()) #2

##Example 17
# name=input("Enter your name")
# print(name.split()) #['Ranjeet', 'Yadav']

##Example 18
# numbers = [5, 10, 15, 20]
# total = sum(numbers, start=10)
# print(total)

##Example 19
# def pin_extractor(poem):
#     secret_code = ''
# poem = """Stars and the moon
# shine in the sky
# white and bright
# until the end of the night"""
# pin_extractor(poem)

##Example 20
# fruits = ['apple', 'plum', 'bananas']
# for index, item in enumerate(fruits):
#     print(index, item)
# 0 apple
# 1 plum
# 2 bananas


##Example 21
# name="name"
# print(name[::-1]) #eman

##Method 2
# s="".join(reversed(name))
# print(s)#eman

##Method 3
# name="Python"
# reverse=""
# for i in range(len(name)-1,-1,-1):
#     reverse=reverse+name[i]
# print(reverse) #nohtyP

##Method 4
# def reverse(s):
#     if len(s)==0:
#         return s
#     return reverse(s[1:])+s[0]
# print(reverse("HELLO"))

##Question 2
# word="1234321"
# is_palindrome=True
# for i in range (len(word)):
#         if word[i]!=word[len(word)-1-i]:
#             is_palindrome=False
# if is_palindrome:
#     print("palindrome")
# else:
#     print("Not palindrome") #palindrome

##Method 2
# word="madam"
# reverse=word[::-1]
# if word[::-1]==word:
#     print("Palindrome")
# else:
#     print("Not Palindrome") #Palindrome

##Method 3
# word="madam"
# reverse=("".join(reversed(word)))
# if reverse==word:
#     print("palindrome")
# else:
#     print("Not palindrome")

##Method 4
# word="madam"
# def palindrome(word):
#     if len(word)<=1:
#         return True
#     if word[0]!=word[-1]:
#         return False
#     return palindrome(word[1:-1])
# if palindrome(word):
#     print("Palindrome")
# else:
#     print("Not palindrome")

##Question 3
# word="i code with python"
# count=0
# for i in ("aeiou"):
#     if i in word:
#         count=count+word.count(i)
# print(count)

##Question 4
# word="i code with python"
# count=0
# for i in ("bcdfghjklmnpqrstvwxyz"):
#     if i in word:
#         count=count+word.count(i)
# print(count)


##Question 5
# word="I Code With Python"
# is_upper_count=0
# is_lower_count=0
# for i in word:
#     if i.isupper():
#         is_upper_count=is_upper_count+word.count(i)
#     elif i.islower():
#         is_lower_count=is_lower_count+word.count(i)
# print(is_upper_count) #4
# print(is_lower_count) #17

##Question 6
# word="i code with python"
# print(word.replace(" ","")) #icodewithpython

##Question 7
# word="i code with python"
# result=""
# for i in word:
#     if i not in "aeiou":
#         result=result+i
# print(result) # cd wth pythn


##Question 8
# word="i code with python"
# for i in word.split():
#     print(i)

# Question 19
# name="hello world"
# count=0
# for i in "aeiou":
#     if i in name:
#         count+=1
# print(count)

##Question 20
# name="name"
# print(name[::-1]) #eman

##Method 2
# s="".join(reversed(name))
# print(s)#eman

##Method 3
# name="Python"
# reverse=""
# for i in range(len(name)-1,-1,-1):
#     reverse=reverse+name[i]
# print(reverse) #nohtyP

##Method 4
# def reverse(s):
#     if len(s)==0:
#         return s
#     return reverse(s[1:])+s[0]
# print(reverse("HELLO"))

##Question 21
# word="1234321"
# is_palindrome=True
# for i in range (len(word)):
#         if word[i]!=word[len(word)-1-i]:
#             is_palindrome=False
# if is_palindrome:
#     print("palindrome")
# else:
#     print("Not palindrome") #palindrome

##Method 2
# word="madam"
# reverse=word[::-1]
# if word[::-1]==word:
#     print("Palindrome")
# else:
#     print("Not Palindrome") #Palindrome

##Method 3
# word="madam"
# reverse=("".join(reversed(word)))
# if reverse==word:
#     print("palindrome")
# else:
#     print("Not palindrome")

##Method 4
# word="madam"
# def palindrome(word):
#     if len(word)<=1:
#         return True
#     if word[0]!=word[-1]:
#         return False
#     return palindrome(word[1:-1])
# if palindrome(word):
#     print("Palindrome")
# else:
#     print("Not palindrome")

##Question 22
# word="i code with python"
# count=0
# for i in ("aeiou"):
#     if i in word:
#         count=count+word.count(i)
# print(count)

##Question 23
# word="i code with python"
# count=0
# for i in ("bcdfghjklmnpqrstvwxyz"):
#     if i in word:
#         count=count+word.count(i)
# print(count)

##Question 24
# word="I Code With Python"
# is_upper_count=0
# is_lower_count=0
# for i in word:
#     if i.isupper():
#         is_upper_count=is_upper_count+word.count(i)
#     elif i.islower():
#         is_lower_count=is_lower_count+word.count(i)
# print(is_upper_count) #4
# print(is_lower_count) #17

##Question 25
# word="PyThon Is EaSy"
# result=""
# for i in word:
#     if i.isupper():
#         result+=i.lower()
#     else:
#         result+=i.upper()
# print(result)#pYtHON iS eAsY

##Question 26
# word="i code with python"
# result=""
# for i in word:
#     if i not in "aeiou":
#         result=result+i
# print(result) # cd wth pythn

##Question 27
# word = "hello"
# for i in word:
#     print(i, ":", word.count(i))

##Question 28
# sentence = "I am learning Python programming"
# words = sentence.split()
# longest = words[0]
# for i in words:
#     if len(i) > len(longest):
#         longest = i
# print("Longest word:", longest)

##Question 29
# sentence = "I love Python"
# words = sentence.split()
# result =[]
# for i in words:
#     result.append(i[::-1])
# print(" ".join(result))#I evol nohtyP

##Question 30
# word = "Hello123@#World45!"
# alphabet = 0
# digit = 0
# special = 0
# for i in word:
#     if i.isalpha():
#         alphabet += 1
#     elif i.isdigit():
#         digit += 1
#     else:
#         special += 1
# print("Alphabets:", alphabet) #10
# print("Digits:", digit)#5
# print("Special characters:", special)#3

##Question 31
# word = "hello    world   python"
# result = " ".join(word.split())
# print(result)#hello world python

##Question 32
# word = "The quick brown fox jumps over the lazy dog"
# word = word.lower()
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i not in word:
#         print("Not Pangram")
#         break
# else:
#     print("Pangram")

##Question 33
# word = "abc12de45f6"
# result = ""
# for i in word:
#     if i.isdigit():
#         result += i
# print(result)#123456

##Question 36
# name="Python"
# s="".join(reversed(name))
# print(s)

##Question 37
# name="madam"
# new_name=name[::-1]
# if name==new_name:
#     print("palindrom")
# else:
#     print("Not palindrom")

##question 38 Unique elements
# name="aeiou aeiou"
# count=0
# for i in "aeiou":
#     if i in name:
#         count+=1
# print(count)

##Method 2 
# name="aeiou aeiou"
# count=0
# for i in name:
#     if i in "aeiou":
#         count+=1
# print(count)



##Questuin 39 Unique consonants count hote hai
# count=0
# name="i code with python"
# for i in "bcdfghjklmnpqrstvwxyz":
#     if i in name:
#         count+=1
# print(count)

##Method 2 for consonants
# count=0
# name="i code with python" 
# for i in name.lower():
#     if i in "bcdfghjklmnpqrstvwxyz":
#         count += 1
# print(count)

##question 40
# name="i code with python"
# new_name=""
# for i in name:
#     if i not in "aeiou":
#         new_name+=i
# print(new_name)# cd wth pythn
