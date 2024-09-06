
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is less than 100
    if a < 100:
        # Check if a is prime
        if a > 1:
            # Check if a is divisible by any number between 2 and 10 except 2 and 5
            for i in range(2, 11):
                if a % i == 0:
                    return False
            return True
    return False