

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Find all divisors of n
    divisors = [2, 4, 6, 8, 10, 15]

    # Find the largest divisor
    while len(divisors) >= 2:
        mid = int(len(divisors) / 2)
        if divisors[mid] * divisors[mid] > n:
            divisors.pop(mid)
        elif n % divisors[mid] == 0:
            return divisors[mid]
        else:
            divisors.pop(mid)

    # If there are no more divisors, return n
    return n
