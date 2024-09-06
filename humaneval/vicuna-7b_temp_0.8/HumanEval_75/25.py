
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is prime
    if a % 2 == 1 or a % 3 == 0:
        return False

    # Check if a is divisible by 4
    if a % 4 == 0:
        return False

    # Check if a is divisible by 6
    if a % 6 == 0:
        return False

    # Check if a is divisible by 9
    if a % 9 == 0:
        return False

    # Check if a is divisible by 10
    if a % 10 == 0:
        return False

    # Check if a is divisible by 11
    if a % 11 == 0:
        return False

    # Check if a is divisible by 12
    if a % 12 == 0:
        return False

    # Check if a is divisible by 13
    if a % 13 == 0:
        return False

    # Check if a is divisible by 14
    if a % 14 == 0:
        return False

    # Check if a is divisible by 15
    if a % 15 == 0:
        return False

    # Check if a is divisible by 16
    if a % 16 == 0:
        return False

    # Check if a is divisible by 17
    if a % 17 == 0:
        return False

    # Check if a is divisible by 18
    if a % 18 == 0:
        return False

    # Check if a is divisible by 19
    if a % 19 == 0:
        return False

    # Check if a is divisible by 20
    if a % 20 == 0:
        return False

    # Check if a is divisible by 21
    if a % 21 == 0:
        return False

    # Check if a is divisible by 22
    if a % 22 == 0:
        return False

    # Check if a is
