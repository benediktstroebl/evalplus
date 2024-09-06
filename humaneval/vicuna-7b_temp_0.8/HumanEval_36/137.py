

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Create a 2D list to store the number of times each number appears in the sequence
    count = [[0] * (10 ** len(str(n)) - 1) for _ in range(n + 1)]

    # Loop through the numbers in the sequence and check if it is divisible by 11 and 13
    for i in range(1, n + 1):
        if i % 11 == 0:
            count[i] = 0
        if i % 13 == 0:
            count[i] = 0
        for j in range(i ** 2, n + 1, i):
            count[j] += 1

    # Return the number of times the digit 7 appears
    return sum(count[i] == 7 for i in range(n + 1))
