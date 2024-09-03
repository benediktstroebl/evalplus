def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    potential_divisors = [1]

    while b > 0:
        for divisor in potential_divisors:
            if a % divisor == 0:
                b //= divisor
                break