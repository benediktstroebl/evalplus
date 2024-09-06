

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while True:
        smallest_even_divisor = max(divisors)
        if n % smallest_even_divisor == 0:
            return smallest_even_divisor
        divisors.append(smallest_even_divisor * 2)
    return 0
