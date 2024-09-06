def is_multiply_prime(a):
    # Check if a is a multiple of 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0: 
        return True
    # If none of the above, return false
    return False