
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # True if a is the multiplication of 3 prime numbers
    # False otherwise

    # iterate through all the numbers between 2 and a-1
    # this will exclude the number a and 1
    for num in range(2, a-1):
        if a % num == 0:
            # if the number is not prime
            return False
    # if no non-prime number is found, return True
    return True
