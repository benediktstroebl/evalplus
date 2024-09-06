

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize an empty list to store the count of 7 and 11
    # since we can't use any built-in list comprehension in python 3.2
    count7 = []
    count11 = []

    # Loop through numbers less than n
    for i in range(1, n):

        # Check if n is divisible by 7, 11, or 13
        if n % 7 == 0:
            count7.append(n)
        elif n % 11 == 0:
            count11.append(n)
        else:
            # If neither of the above conditions are met, add n to the count7 and count11 lists
            count7.append(n)
            count11.append(n)

    # Return the count of 7 and 11
    return (count7, count11)
