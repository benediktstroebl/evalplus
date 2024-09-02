
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
    # Let's start by converting the input to strings
    a_str = str(a)
    b_str = str(b)
    # Now, we can use a for loop to iterate through the strings
    # and compare the rightmost digits
    for i in range(max(len(a_str), len(b_str))):
        if a_str[i] == b_str[i]:
            # We found a match, so we can just multiply the
            # corresponding units digits and add the result to our product
            product += a_str[i] * b_str[i]
        else:
            # We didn't find a match, so the unit digits are 0,
            # and we can just add the corresponding values
            product += a_str[i] * b_str[i]
    return product
