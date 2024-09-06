def is_multiply_prime(a):
    # Check if a is a multiple of 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return True
    # Check if a is a multiple of any other prime number less than 100
    for i in range(2, 100):
        if a % i == 0:
            return True
    return False