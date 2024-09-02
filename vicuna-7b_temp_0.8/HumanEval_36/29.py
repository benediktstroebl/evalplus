

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a list of the numbers 1-100
    numbers = list(range(1, 101))

    # Initialize a variable to keep track of how many times 7 appears
    num_7 = 0

    # Loop through the numbers in the list
    for num in numbers:
        # If the number is divisible by 11, it is divisible by 11 or 13, so it counts as 11 or 13
        if num % 11 == 0:
            num = 11
        # If the number is divisible by 13, it is divisible by 11 or 13, so it counts as 11 or 13
        if num % 13 == 0:
            num = 13
        # If the number is 7, it counts as 7
        if num == 7:
            num_7 += 1

    return num_7
