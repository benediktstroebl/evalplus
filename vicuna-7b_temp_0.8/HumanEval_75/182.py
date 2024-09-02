
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if the number is prime
    if a % 2 == 0 or a % 3 == 0:
        return False
    # Check if the number is divisible by 5
    if a % 5 == 0:
        return False
    # Check if the number is divisible by 3
    if a % 3 == 0:
        for i in range(6, int(a ** 0.5) + 1, 3):
            if a % i == 0:
                return False
    # Check if the number is the product of two prime numbers
    for i in range(2, int(a ** 0.5) + 1, 2):
        for j in range(2, int(a ** 0.5) + 1, 2):
            if a == i * j:
                return True
    return True
