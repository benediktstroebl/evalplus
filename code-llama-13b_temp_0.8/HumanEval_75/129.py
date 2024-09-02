
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 0:
        number = 1
        multipliers = 0
        while number < a:
            if a % number == 0:
                multipliers += 1
            number += 1
        return multipliers == 3
    return False
