

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is a prime number
    if not n % 2:
        return n

    # Find the largest number that divides n evenly
    while n > 1:
        # Check if n % i is equal to 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            n //= i

    return n
