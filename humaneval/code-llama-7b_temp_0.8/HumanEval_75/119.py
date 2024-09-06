
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Create a list of primes up to 10
    prime_list = [2, 3, 5, 7]

    # Check if the given number is a product of 3 primes
    for p in prime_list:
        while a%p == 0:
            a = a / p
            if a == 1:
                return True
        return False

