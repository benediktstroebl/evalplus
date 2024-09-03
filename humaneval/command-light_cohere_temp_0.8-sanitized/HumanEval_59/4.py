def largest_prime_factor(n: int):
    if n <= 1:
        return 1
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return max(largest_prime_factor(n // 2), largest_prime_factor(n // 3))
    else:
        return [7, 11, 13][:int(n ** 0.25)]