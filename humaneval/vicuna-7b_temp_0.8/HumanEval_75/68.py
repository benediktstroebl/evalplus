
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if len(prime) < a - 1:
        return False

    for i in range(a - 1):
        if a % prime[i] == 0:
            return False

    return True