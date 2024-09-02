

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while True:
        # check if the number is divisible by the current divisor
        if n % divisors[0] == 0:
            # if so, find the largest divisor that is less than or equal to n
            largest_divisor = min(divisors)
            break
        else:
            # add the next largest divisor to the list
            divisors.append(divisors[-1] + 1)
    return largest_divisor
