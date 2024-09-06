def is_multiply_prime(a):
    # check if a is a multiple of 2
    if a % 2 == 0:
        return False

    # check if a is a multiple of 3
    if a % 3 == 0:
        return False

    for i in range(5, int(a**0.5) + 1):
        if a % i == 0:
            return False

    return True