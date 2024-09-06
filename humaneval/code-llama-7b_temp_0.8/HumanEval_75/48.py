
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Step 1: Verify that (a) is the multiplication of 3 prime numbers:
    # Step 1a: Verify that (a) is the multiplication of 2 prime numbers:
    if not is_prime(a): return False
    # Step 1b: Verify that (a) is the multiplication of 3 prime numbers:
    while a != 1:
        for i in range(2,a+1):
            if a%i == 0:
                a = a//i
                break
        else:
            return False
    return True
