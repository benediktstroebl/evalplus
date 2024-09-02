

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Create a list of all the numbers from 1 to n, excluding 1
    numbers = range(2, n+1)

    # Create a dictionary to count the number of times each number is divisible by 7
    counts = {7: 0, 11: 0, 13: 0}

    # Loop through the numbers and count the number of times 7, 11, 13 appear
    for num in numbers:
        if num % 7 == 0:
            counts[7] += 1
        elif num % 11 == 0:
            counts[11] += 1
        else:
            counts[13] += 1

    # Return the number of times 7 appears in the numbers
    return counts[7]
