

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Build a list of divisors
    divisors = [1, 2, 3, 4, 6, 8, 9, 11, 12, 14, 16]

    # Build a list of numbers less than n that are divisible by 11 or 13
    numbers = [i for i in range(1, n+1) if i % 11 == 0 or i % 13 == 0]

    # Iterate through the numbers
    for i in numbers:
        # If the number is divisible by 7, we have 0 fizz, 0 buzz
        if i % 7 == 0:
            print(0, end=' ')
        # If the number is divisible by 11, we have 0 fizz, 1 buzz
        elif i % 11 == 0:
            print(1, end=' ')
        # If the number is divisible by 13, we have 0 fizz, 2 buzz
        elif i % 13 == 0:
            print(2, end=' ')
        # If the number is divisible by 7 and 11, we have 3 fizz, 1 buzz
        elif i % 7 == 0 and i % 11 == 0:
            print(3, end=' ')
        # If the number is divisible by 7 and 13, we have 0 fizz, 3 buzz
        elif i % 7 == 0 and i % 13 == 0:
            print(3, end=' ')
        # If the number is divisible by 11 and 13, we have 1 fizz, 2 buzz
        elif i % 11 == 0 and i % 13 == 0:
            print(1, 2, end=' ')
        # Otherwise, we have the number itself
        else:
            print(i, end=' ')

    # Print the final buzz or fizz
    if divisors[-1] % 11 == 0:
        print(4, end=' ')
    elif divisors[-1] % 13 == 
