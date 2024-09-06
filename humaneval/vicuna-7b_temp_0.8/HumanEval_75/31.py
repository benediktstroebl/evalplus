
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if the number is divisible by any number other than 1 and itself
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False
    # Check if the number is divisible by 3
    if a % 3 == 0:
        # Check if the number is divisible by 9
        if a % 9 == 0:
            # Check if the number is divisible by 3 times the smallest prime factor
            if a % (3 * min(a//3)) == 0:
                return True
            else:
                return False
    # Check if the number is divisible by 5
    if a % 5 == 0:
        # Check if the number is divisible by 5 times the smallest prime factor
        if a % (5 * min(a//5)) == 0:
            return True
        else:
            return False
    # Check if the number is divisible by 7
    if a % 7 == 0:
        # Check if the number is divisible by 7 times the smallest prime factor
        if a % (7 * min(a//7)) == 0:
            return True
        else:
            return False
    # Check if the number is divisible by 11
    if a % 11 == 0:
        # Check if the number is divisible by 11 times the smallest prime factor
        if a % (11 * min(a//11)) == 0:
            return True
        else:
            return False
    return False
