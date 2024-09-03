def largest_prime_factor(n: int):
    if n <= 1:
        return 1
    if n <= 3:
        return 3
    # check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return max(2, 3)
    # n must be odd
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return 2