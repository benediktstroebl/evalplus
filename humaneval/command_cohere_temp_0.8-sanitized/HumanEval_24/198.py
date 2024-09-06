def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # n // i gives the same value as math.gcd but is usually slower
            if j > i:
                return i
            if j < i:
                return j
    return 1  # If no divisors are found, return 1