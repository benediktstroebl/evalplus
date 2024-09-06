

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # n is odd, find the largest odd number that is less than or equal to n
    while True:
        if n % 2 == 0:
            break
        n /= 2
        largest_even_divisor = largest_divisor(n)
        if n == largest_even_divisor:
            return n
        n //= 2
    # n is even, find the largest even number that is less than or equal to n
    largest_even_divisor = largest_divisor(n)
    if n == largest_even_divisor:
        return n
    n //= 2
    while True:
        if n % 2 == 0:
            break
        n /= 2
        largest_even_divisor = largest_divisor(n)
        if n == largest_even_divisor:
            return n
        n //= 2
    # n is odd, find the largest odd number that is less than or equal to n
    largest_odd_divisor = max(range(3, n + 1))
    if n % largest_odd_divisor == 0:
        return largest_odd_divisor
    return largest_odd_divisor - 1
