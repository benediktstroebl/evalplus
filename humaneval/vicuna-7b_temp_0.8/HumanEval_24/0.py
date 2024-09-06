

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [x for x in range(1, n + 1) if n % x == 0]
    max_index = 0
    max_value = n
    for i in range(1, len(divisors)):
        if divisors[i] > max_value:
            max_value = divisors[i]
            max_index = i
    return max_value
