def is_multiply_prime(a):
    # Check if a is a perfect square
    root = int(pow(a, 0.5))
    if root * root == a:
        return False

    # Check for divisibility by 2 and 3
    if a % 2 == 0 or a % 3 == 0:
        return False

    # Check for prime factors
    for i in range(5, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True