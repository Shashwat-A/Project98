# f = open("test.txt", "a")
# l = ["I like python"]
# f.writelines(l)
# f.close()
# # a is appending





# string = "My name is Shashwat, I am 14 years old" 
# words = string.split()
# print(words)
# we can use different things as spliters but by default its space





# string = "My name is Shashwat, I am 14 years old" 
# words = string.split(",")
# print(words)





# # name is parameter 
# def greet(name):
#     print("Hello", name, ".How are you ?")

# greet("Shashwat")





# filename = input("Input the filename.")
# count = 0
# filetxt = "nothing"

# def dd () :
#     file = open(filename)
#     file.read()
#     filetxt = file.read()

#     for charcter in filetxt :
#         count = count + 1
    

# dd()
# print(count)





# def countWords () :
#     filename = input("Enter File Name -")
#     totalwords = 0
#     file =  open(filename, "r")
    
#     for line in file :
#         words = line.split()
#         totalwords = totalwords + len(words)

#     print(len(words))
#     print("Number of words -", totalwords) 

# countWords()





def contentSwap() :
    file1Name = input("Enter file 1.")
    file2Name = input("Enter file 2.")

    file1 = open(file1Name, "r")
    file2 = open(file2Name, "r")
    file1Data = file1
    file2Data = file2
    file1Write = open(file1Name, "w")
    file1Write.writelines(file2Data)
    file2Write = open(file2Name, "w")
    file2Write.writelines(file1Data)

contentSwap()