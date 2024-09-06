

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # divide the number by the first 5 integers and check if the remainder is zero
    # if it is, it is the largest divisor
    divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0
    while i < len(divisors) and divisors[i] % n != 0:
        i += 1
    if i == len(divisors):
        return n
    else:
        # if n is not divisible by any of the first 5 integers, try the first 6
        divisors.extend([11, 12, 13, 14, 15])
        i = 0
        while i < len(divisors) and divisors[i] % n != 0:
            i += 1
        if i == len(divisors):
            return n
        else:
            # if n is not divisible by any of the first 10 integers, return n
            return n
