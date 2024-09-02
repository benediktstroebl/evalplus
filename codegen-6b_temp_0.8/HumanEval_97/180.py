
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
    # Declare your variables
    c = 0
    # Insert your code here
    lst_a = [int(i) for i in str(a)]
    lst_b = [int(i) for i in str(b)]
    for i in range(len(lst_a)):
        c += lst_a[len(lst_a)-i-1] * lst_b[i] 
    return c
