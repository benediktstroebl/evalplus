

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        # find the largest number that is less than or equal to n
        max_val = min(n, (n - 1) // 2)
        # check if the number is a divisor of n
        if max_val % n == 0:
            return max_val
        # increase the value of n by 1 and repeat the process
        n += 1
        
    return n