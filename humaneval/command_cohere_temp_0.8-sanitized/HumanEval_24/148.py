def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Largest divisor found, now checking if there's a larger one
            if j > i:  # There is, because of the division behavior for larger divisors
                return j
            else:
                return i
    else:
        return 1  # If no divisor is found, return 1