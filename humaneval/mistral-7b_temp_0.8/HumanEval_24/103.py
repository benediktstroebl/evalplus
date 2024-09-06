

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # 1. write a for loop that iterates from 1 to n-1
    # 2. for every number x in the range, if n % x == 0 return x
    # 3. if there is no return, return n

    for i in range(1, n):
        if n % i == 0:
            return i

    return n

