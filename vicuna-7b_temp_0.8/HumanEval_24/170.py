

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2]
    for num in divisors:
        while (n // num) % num != 0:
            divisors.append(num + 1)
            n = n // num
    return divisors[0]
