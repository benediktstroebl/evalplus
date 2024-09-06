
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    #First heuristics: we can skip the integers whose modulo is zero
    if a % 2 == 0:
        return False
    for a_prime in [2,3,5]:
        while a % a_prime == 0:
            a /= a_prime
        if a == 1:
            return True
    return False
