                            # WAP to chek number present in list or not.

def find_num(num,list):
    for element in list :
        if num == element :
            print("Number Found")  
            break
    else:
        print("Number not Found")

list = [10,15,30,23,5,50]
num = int(input("Enter the number :"))

find_num(num,list)
