

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # My First approach
    # largest_divisor = n
    # for i in range(n-1, 1, -1):
    #     if n % i == 0:
    #         largest_divisor = i
    #         break
    # return largest_divisor

    # My Second approach
    # for i in range(n//2, 0, -1):
    #     if n % i == 0:
    #         return i
    # return n

    # My Third approach
    return int(math.sqrt(n))

