
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Declare the variables
    result = False
    check_number = 2

    # Loop through the prime numbers until you reach the desired one
    while not result and check_number < 3:
        if a % check_number == 0:
            check_number += 1
            continue
        check_number += 1
        result = True
    return result

