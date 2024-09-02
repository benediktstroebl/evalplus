
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is prime
    if a != 1 and not is_prime(a):
        return False

    # Check if a is a perfect square
    if (a**2) == a:
        return True

    # Find the first digit that is greater than 1
    digit = 1
    while not digit**a:
        digit += 1

    # Find the second digit that is greater than 1
    digit = 1
    while not (digit**a and (digit**a)**a != a):
        digit += 1

    # Find the third digit that is greater than 1
    digit = 1
    while not (digit**a and (digit**a)**a and (digit**a)**a != a):
        digit += 1

    # Check if the first digit is 1
    if digit == 1:
        return True

    # Check if the second digit is 1
    if (digit**a) % 2 == 1:
        return True

    # Check if the third digit is 1
    if (digit**a) % 2 == 1 and (digit**a) % 3 == 1:
        return True

    # Return False if none of the above conditions are met
    return False
