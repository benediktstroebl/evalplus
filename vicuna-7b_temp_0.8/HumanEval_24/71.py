

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # base case
    if n == 1:
        return 1
    # loop over all numbers up to sqrt(n)
    for i in range(1, int(n**0.5)+1):
        # check if n is divisible by i
        if n % i == 0:
            # check if i is the largest divisor
            if i > max(divisors(n//i)) or i > n//i:
                return i
    # if no divisor is found, return n
    return n
