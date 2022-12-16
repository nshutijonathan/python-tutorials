# file=open('example.txt')
# print("file",file.read())
# file.close()

with open('example.txt') as file:
    for item in file:
        print("item",item)