

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    divisors = list(range(1, n+1))
    largest = 0
    while True:
        for d in divisors:
            if n % d == 0:
                largest = d
            else:
                break
        return largest

