def is_multiply_prime(a):
    # check if a is less than 100
    if a < 100:
        # manually check for each prime number multiplication
        for i in range(2,a):
            if a % i == 0:
                return False
        return True
    else:
        return False