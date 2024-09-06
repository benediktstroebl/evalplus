
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
    #Input: 2 integers
    #Output: product of unit digits

    #Run through the values and find the unit digits.
    #Multiply the unit digits and return.
    a = int(a)
    b = int(b)

    a = a % 10
    b = b % 10

    product = a * b

    return product
