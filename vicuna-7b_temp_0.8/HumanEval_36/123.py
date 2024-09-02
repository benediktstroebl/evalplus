

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a variable to store the number of times 7 appears
    # Initialize a variable to store the number of times 11 appears
    # Initialize a variable to store the number of times 13 appears
    # Initialize a variable to store the number of times 11 and 13 appear together
    num7 = 0
    num11 = 0
    num13 = 0
    num11_and_13 = 0
    for i in range(n):
        # If the number is divisible by 7, set the num7 variable to 1
        if i % 7 == 0:
            num7 += 1
        # If the number is divisible by 11, set the num11 variable to 1
        if i % 11 == 0:
            num11 += 1
        # If the number is divisible by 13, set the num13 variable to 1
        if i % 13 == 0:
            num13 += 1
        # If the number is divisible by 7, 11, and 13, set the num11_and_13 variable to 1
        elif i % 7 == 0 and i % 11 == 0 and i % 13 == 0:
            num11_and_13 += 1
    
    # Print the number of times 7 appears
    print(num7)
    
    # Print the number of times 11 appears
    print(num11)
    
    # Print the number of times 13 appears
    print(num13)
    
    # Print the number of times 11 and 13 appear together
    print(num11_and_13)