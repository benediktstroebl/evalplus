

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # check if n is positive
    if n <= 0:
        return 0

    # check if n is prime
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1

    # check if n is even
    if n % 2 == 0:
        return 2*sum_to_n(n//2)

    # check if n is odd
    if n % 2 != 0:
        return sum_to_n(n//2) + sum_to_n(n//2 + 1)

    # sum
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
