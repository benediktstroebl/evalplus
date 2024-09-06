def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    if n == 1:
        return 1
    for i in range(1, n + 1):
        if n % i == 0 and n // i >= i:
            return i
    return 1