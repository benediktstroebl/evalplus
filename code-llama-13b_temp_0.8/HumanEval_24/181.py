

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # print("Checking divisors of", n)
    # We can stop the search at sqrt(n) because a divisor of n must be smaller than this
    max_divisor = int(n / 2)

    for divisor in range(max_divisor, 1, -1):
        if n % divisor == 0:
            # print("Found a perfect divisor:", divisor)
            return divisor

    return 1

