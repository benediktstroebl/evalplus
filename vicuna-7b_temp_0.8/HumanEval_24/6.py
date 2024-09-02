

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # check if n is 0 or 1
    if n == 0 or n == 1:
        return 1
    
    # find the largest divisor that is smaller than n
    largest = 1
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            # if the largest divisor is equal to the input n,
            # we cannot find a larger one
            if largest == n:
                return n
            # update the largest divisor
            largest = num
    # if we reach here, we cannot find a larger divisor
    return largest
