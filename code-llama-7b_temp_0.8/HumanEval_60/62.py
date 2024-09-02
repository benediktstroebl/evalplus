

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
    # Loop invariant: sum is the sum of integers from 1 to i, inclusive
    # sum stores the current sum, which starts at 0 and is updated each time through the loop
    # i stores the number of times through the loop, starting at 1 and ending when i == n + 1
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

