def largest_divisor(n: int) -> int:
    """ Efficiently finds the largest divisor of a number """
    def is_prime(num):
        if num < 4:
            return num < 4
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if is_prime(n):
        return 1  # Primes have only 1 as a factor
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and n // i > i:
            return n // i
    return n  # No divisors found, return n