def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    if a < 3:
        return False
    for i in range(2, int(a**.5()) + 1):
        if a % i == 0:
            return False
    return True