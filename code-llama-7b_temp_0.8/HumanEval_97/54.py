
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
    str1 = str(a)
    str2 = str(b)
    product = 0
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if int(str1[i]) == int(str2[j]):
                product += int(str1[i])
    return product
