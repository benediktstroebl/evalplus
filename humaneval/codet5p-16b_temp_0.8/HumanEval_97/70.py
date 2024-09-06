
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    num1 = str(a)
    num2 = str(b)
    list1 = []
    list2 = []
    sum = 0
    for i in num1:
        list1.append(int(i))
    for i in num2:
        list2.append(int(i))
    for j in range(len(list1)):
        sum += list1[j] * list2[j]
    return sum
