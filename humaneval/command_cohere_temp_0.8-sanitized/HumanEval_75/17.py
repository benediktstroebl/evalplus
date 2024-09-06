def is_multiply_prime(a):
    # check if a is divisible by 2 or 3
    if a % 2 == 0 or a % 3 == 0: 
        return False

    # check if a is divisible by any number in the range 5 to sqrt(a)
    for i in range(5, int(np.sqrt(a)) + 1, 6):
        if a % i == 0 or a % (i + 2) == 0: 
            return False

    return True