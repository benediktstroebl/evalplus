

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # largest = n // 2
    # while largest >= 1:
    #     if n % largest == 0:
    #         return largest
    #     largest -= 1
    largest = 1
    while largest < n:
        if n % largest == 0:
            break
        largest += 1
    return largest

