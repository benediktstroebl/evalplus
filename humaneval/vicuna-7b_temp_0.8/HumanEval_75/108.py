
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Loop from 2 to a/2
    for i in range(2, a // 2 + 1):
        # Check if a is divisible by i
        if not (a % i == 0):
            return False
    # Check if a is divisible by 3
    if a % 3 == 0:
        return False
    # Loop from 5 to (a - 1) / 2
    for j in range(5, (a - 1) // 2 + 1):
        # Check if a is divisible by 3 * j
        if a % (3 * j) == 0:
            return False
    # If no divisor was found, return True
    return True