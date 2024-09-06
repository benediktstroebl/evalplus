def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if the root of a is an integer
        if int(a**(1/3)) == a**(1/3):
            # Check if a is the multiplication of 3 prime numbers
            if a != 1: 
                return all([p == a % p for p in range(2, int(a**(1/3) + 1))])
        else:
            return False
    else:
        return False