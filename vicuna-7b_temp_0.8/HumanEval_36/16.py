

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Base case: n < 11
    if n < 11:
        return 1
    # Find the number of times the digit 1 appears
    num1s = 0
    for i in range(n // 11):
        if n % 11 == 0:
            num1s += 1
    # Find the number of times the digit 2 appears
    num2s = 0
    for i in range((n + 1) // 11):
        if (n + 1) % 11 == 0:
            num2s += 1
    # Use modulo to find the number of times the digits 1 and 3 appear
    num13s = 0
    for i in range(n // 13):
        if (n + 1) % 13 == 0:
            num13s += 1
    # Combine the above logic to find the number of times all other digits appear
    numothers = 0
    for i in range(1, 10):
        numothers += (n // i) % i
    # Combine the above logic to find the number of times 7 appears
    num7s = 0
    for i in range(n // 7):
        if n % 7 == 0:
            num7s += 1
    # Return the result
    return (num1s + num2s + num13s + numothers - 7) % 11