def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    if a < 100 and a != 1:
        # Splitting into three parts for quicker exploitation of the modular arithmetic properties
        for i in range(2, int(a ** (1/3)) + 1):
            if a % i == 0:
                return False
        for i in range(2, int(a ** (1/3)) + 1):
            if a % i == 0:
                return False
        return True
    return False