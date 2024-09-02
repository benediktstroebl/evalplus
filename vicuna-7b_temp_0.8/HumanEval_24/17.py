

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while n > 1:
        divisors.append(n % (n // i) for i in range(1, n + 1) if n % i == 0)
        n //= i
    return max(divisors, key=lambda x: x if x == n else x - 1)

