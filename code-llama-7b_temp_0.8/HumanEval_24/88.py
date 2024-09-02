

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # largest_divisor = n
    for i in range(n - 1, 0, -1):
        # if n % i == 0:
        #     largest_divisor = i
        #     break
        if n % i == 0:
            return i

