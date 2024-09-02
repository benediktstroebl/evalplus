

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_value = 1
    max_index = 0
    for i in range(1, n+1):
        if n % i == 0:
            max_value = i
            max_index = i
    return max_value
