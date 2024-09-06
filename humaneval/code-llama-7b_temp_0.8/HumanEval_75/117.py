
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # prime numbers are divisible by 1 and themselves
    for divisor in range(2, a):
        # check if (a) is divisible by (divisor)
        if a % divisor == 0:
            # if it is, we're not done yet
            # let's check the rest
            continue
        # if none of the divisors divided (a), we're done
        return False
    return True
