

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 4:
        return 1
    else:
        # check if n is divisible by 2
        if n % 2 == 0:
            return 2
        # check if n is divisible by 3
        elif n % 3 == 0:
            return 3
        # n is not divisible by 2 or 3
        else:
            divisor = n//3
            # loop over the numbers between 2 and the divisor to find a number
            # that n is divisible by
            while divisor > 1:
                if n % divisor == 0:
                    return divisor
                else:
                    divisor -= 1



