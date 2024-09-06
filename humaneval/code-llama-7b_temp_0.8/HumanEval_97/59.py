
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
    result = ""
    for i in range(len(a)):
        if (a[i] != "0") and (b[i] != "0"):
            result += str(int(a[i])*int(b[i]))
    for i in range(len(result)):
        result[i] = int(result[i])
    return sum(result)
