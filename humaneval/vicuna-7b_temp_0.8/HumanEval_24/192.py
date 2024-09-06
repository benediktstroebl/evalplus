

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is 0
    if n == 0:
        return 0
    # Check if n is 1
    if n == 1:
        return 1
    # Check if n is prime
    if n % 2 == 0:
        return 0
    # Find divisors of n
    divisors = [2]
    for i in range(3, int(n ** 0.5) + 1, 2):
        divisors.append(i)
    # Find the largest divisor
    max_divisor = 0
    for d in divisors:
        if d > max_divisor:
            max_divisor = d
    return max_divisor
