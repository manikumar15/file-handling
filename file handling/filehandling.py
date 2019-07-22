# FILE HANDLING:
# --------------------------
# 1.Creating A Text File Using Python:

# file = open("demo.txt","w") 
# file.write("Hello mom Happy Diwali\n") 
# file.write("madam This is our new text file madam\n") 
# file.write("Happy mom\n") 
# file.write("Diwali.") 
# file.close()
# -----------------------------------------------------------------------------------------
# 2.Reading A Text File In Python and display output in cmd:

# file = open("demo.txt", "r") 
# for line in file: 
# 	print(line)
# ------------------------------------------------------------------------------------------------
# 3.read the data in text file:	it may read upto first 5 lines:

# file = open("demo.txt", "r")
# print(file.read(5))
# --------------------------------------------------------------------------------------------------
# 4.To add more text line by line:

# file = open("demo.txt", "w")
# file.write("Enjoy weekend\n") 
# file.write("too make Fun.")
# file.close()
# --------------------------------------------------------------------------------------------
# 5.Splitting Lines In A Text File:

# with open("demo.txt", "r") as f:
# 	data = f.readlines()
# 	for line in data:
# 		words = line.split()
# 		print(words)
# -------------------------------------------------------------------------------------------------------
# 6.count number of words in text file:

# fname = input("Enter your name: ")
# num_words = 0
# with open("demo.txt", 'r') as f:
#     for line in f:
#         words = line.split()
#         num_words += len(words)
# print("Number of words:")
# print(num_words)
# ----------------------------------------------------------------------------------------------------------
# 7.print all the words in a file with the number of times repeated in python test only on by one:

# fname = input("Enter your name: ")
# word=input("Enter word to be searched:")
# k = 0
 
# with open("demo.txt", 'r') as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             if(i==word):
#                 k=k+1
# print("Occurrences of the word:")
# print(k)
# -----------------------------------------------------------------------------------------------
# 8.print all the words in a file with the number of times repeated in python for all strings:

# import re
# import string
# frequency = {}
# document_text = open('demo.txt', 'r')
# text_string = document_text.read().lower()
# match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
# for word in match_pattern:
#     count = frequency.get(word,0)
#     frequency[word] = count + 1
     
# frequency_list = frequency.keys()
 
# for words in frequency_list:
#     print(words,"=",frequency[words])
# ---------------------------------------------------------------------------------------
# 9.print all the palindrome words in a file in python and count number of times repeated:

# from collections import Counter

# def isPalindrome(s): 
#     if (s == s[::-1] ): return True
#     else: return False

# def findPalindrome(): 
#     list3=list() 
#     for line in open("demo.txt"): 
#         list1 = line.strip() 
#         list2 = list1.split() 
#         for x in list2:
#             if isPalindrome(x): 
#                 list3.append(x) 

#     return list3 

# palim_list = findPalindrome()
# palim_counts = Counter(palim_list)
# print(palim_list)
# print (palim_counts)
# -------------------------------------------------------------------------------------
# 10.print an longest palindrome in a file:

# with open('demo.txt','r') as f:
#     x=f.read()
# words=list(x.split(' '))
# uniquewords=set(words)
# palindromewords=set()
# wordlength=[]

# wordlength=[]
# for i in uniquewords:
#     if i ==i[::-1] and len(i)>=3:
#         palindromewords.add(i)
#         wordlength.append(len(i))
# for i in palindromewords:
#     if len(i)==max(wordlength):
#         print(i,"=",words.count(i))
# ----------------------------------------------------------------------------------------
# 11. virat was notout matches:

# a=[['14/2/9','out',46,'yuvaraj'],['15/3/8','notout',49,'virat']]

# count=0
    
# for i in a:
#     if i[1] == 'notout':
#         count=count+1
# print('notout of virat in matches :',count)
# -----------------------------------------------------------------------------------------