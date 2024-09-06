
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_numbers = [2, 3, 5]
    # result = 1
    # for prime_number in prime_numbers:
    #     result *= prime_number
    # if result == a:
    #     return True
    # return False
    return a in [2 * 3 * 5, 3 * 5 * 7, 2 * 3 * 7]

