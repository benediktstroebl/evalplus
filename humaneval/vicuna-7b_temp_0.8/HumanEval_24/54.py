

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_digit = 0
    for digit in str(n):
        largest_digit = max(largest_digit, digit)
        n //= digit
    return n // largest_digit
