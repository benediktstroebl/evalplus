
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
    
    # Reversed number, not a string.
    a = int(a[::-1])
    b = int(b[::-1])
    
    # Value for multiplying together.
    c = 0
    
    # Loop until both numbers are equal or b < a.
    while a != b:
        # Return any remainder.
        if a < b:
            return c
        
        # Restart at 0.
        if c > 0:
            c = 0
        
        # Add the lowest digit of both numbers.
        c += (a % 10) * (b % 10)
        
        # Numerically correct, but only before 10.
        a = a // 10
        b = b // 10

    return c


assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14, -15) == 20
