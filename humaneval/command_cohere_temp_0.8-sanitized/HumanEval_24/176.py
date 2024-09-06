def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Largest divisor found, now checking if there's a larger one
            if j == i:  # No division possible, so i is the largest divisor
                return i
            if j > i:  # Found a larger divisor
                return j
    return 1  # No divisors found, return 1