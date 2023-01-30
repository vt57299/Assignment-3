
# Quest_1 = Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# Explanation:
# Summation should like 8+2+3+0+7 = 20


def summation():
    lst = []
    size = int(input("Enter size: "))
    
    for i in range(size):
        elements  = int(input("Enter elements: "))
        lst.append(elements)
    print("Your list: ", lst)

    result = 0
    for j in range(len(lst)):
        number = lst[j]
        result += number
        if j != len(lst) - 1:                  # As soon as "j" reaches the last element of list it will go to the else part.
            print(number, end=" + ")
        else:
            print(number, end=" = ")
    # print(result)
    return result

sum = summation()
print("Summation: ", sum)