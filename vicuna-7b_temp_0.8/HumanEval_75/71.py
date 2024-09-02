
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

    # Check if a is equal to 3
    if a == 3:
        return True

    # Check if a is equal to a^2
    if a == pow(a, 2):
        return is_multiply_prime(a - 1) and is_multiply_prime(a - 2)

    # Check if a is equal to 2*3*5
    for i in range(3, int(a**0.5)+1, 2):
        if a % i == 0:
            return False

    return True
