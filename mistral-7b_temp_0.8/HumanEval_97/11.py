
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
    # digits = []
    # num = a
    # while num > 0:
    #     digits.append(num%10)
    #     num = num//10

    # result = 0
    # for i in range(0, len(digits)):
    #     result += digits[i] * digits[len(digits)-1-i]

    # return result

    digits1 = []
    digits2 = []
    num1 = a
    while num1 > 0:
        digits1.append(num1%10)
        num1 = num1//10

    num2 = b
    while num2 > 0:
        digits2.append(num2%10)
        num2 = num2//10

    result = 0
    for i in range(0, len(digits1)):
        result += digits1[i] * digits2[len(digits1)-1-i]

    return result


