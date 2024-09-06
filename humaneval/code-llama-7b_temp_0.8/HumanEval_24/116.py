

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    #ensure n is an integer
    if not isinstance(n, int):
        raise TypeError(f"n must be of type int, not {type(n)}")

    #if n is less than 1, raise ValueError
    if n < 1:
        raise ValueError(f"n must be positive")

    #if n is 1, return n
    if n == 1:
        return n

    #if n is even, divide n by 2 and return largest_divisor
    if n % 2 == 0:
        return largest_divisor(n // 2)

    #set current_largest_divisor to n
    current_largest_divisor = n

    #iterate through all numbers smaller than n
    for i in range(3, n, 2):
        #if n is divisible by i, and divisible by largest_divisor, set largest_divisor to i
        if n % i == 0 and n % current_largest_divisor == 0:
            current_largest_divisor = i

    #return largest_divisor
    return current_largest_divisor
