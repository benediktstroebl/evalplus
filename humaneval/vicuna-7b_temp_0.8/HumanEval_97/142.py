
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
    assert a > 0 and b > 0, 'Invalid input'
    
    # Convert input to string in base 10
    a_str = str(int(a))
    b_str = str(int(b))
    
    # Initialize result to zero
    result = 0
    
    # Loop through each digit of the input string
    for i in range(max(len(a_str), len(b_str))):
        # Compare the digits of the input string
        if a_str[i] > b_str[i]:
            # Exchange the digits if necessary
            a_str, b_str = b_str, a_str
        result = result * 10 + int(a_str[i]) - int(b_str[i])
    
    # Convert the result back to an integer
    return int(result)
