def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  # i is the largest divisor
            return i if j == 1 else j
    return 1  # If no divisors are found, return 1