

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while True:
        i = (n // divisors[0]) % 2
        if i == 0:
            return divisors[0]
        if n % divisors[0] != 0:
            break
        divisors.append(divisors[0])
    return n