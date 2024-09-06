def is_multiply_prime(a):
    # Check if a is a multiple of 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0: 
        return True
    # If a is not divisible by 2, 3, or 5, then it is not a multiply prime
    return False