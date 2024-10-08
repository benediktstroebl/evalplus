
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is prime
    if not is_prime(a):
        return False

    # If a is prime, check if the factors are 3 and 5
    factors = []
    for i in range(2, a):
        if a % i == 0:
            factors.append(i)

    if len(factors) == 2 and factors[0] == 3 and factors[1] == 5:
        return True

    return False
