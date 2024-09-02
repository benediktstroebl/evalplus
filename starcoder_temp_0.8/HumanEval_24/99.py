

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # initialize an answer with 1 (a factor of 1 is also a factor of every number)
    ans = 1
    # start a divisor at 2
    divisor = 2
    # keep going as long as the divisor is less than or equal to n
    while divisor <= n:
        # if n is divisible by the current divisor, update ans
        if n % divisor == 0:
            ans = divisor
        # increment the divisor
        divisor += 1
    # once the while loop finishes, return ans
    return ans
