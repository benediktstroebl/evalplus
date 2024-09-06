

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is divisible by 2
    if n % 2 == 0:
        return 2
    # Check if n is divisible by 3
    if n % 3 == 0:
        return 3
    # Check if n is divisible by 4
    if n % 4 == 0:
        return 4
    # Check if n is divisible by 5
    if n % 5 == 0:
        return 5
    # Check if n is divisible by 6
    if n % 6 == 0:
        return 6
    # Check if n is divisible by 7
    if n % 7 == 0:
        return 7
    # Check if n is divisible by 8
    if n % 8 == 0:
        return 8
    # Check if n is divisible by 9
    if n % 9 == 0:
        return 9
    # Check if n is divisible by 10
    if n % 10 == 0:
        return 10
    # If n is not divisible by any of the above numbers, return the largest number
    return max(range(1, int(n**0.5)+1), key=lambda x: x % n)
