
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Multiply Prime Numbers : 2, 3, 5, 7
    # 2 * 3 * 5 = 30
    # 2 * 3 * 7 = 42
    # 2 * 3 * 7 = 42
    # 2 * 5 * 7 = 70
    # 3 * 5 * 7 = 105
    # 2 * 3 * 5 * 7 = 210
    prime_list = [2, 3, 5, 7]
    for prime_number in prime_list:
        # Checking if a can be divided by prime number.
        if not a % prime_number:
            a = a / prime_number
            return True
        # If a can't be divided by prime_number, then return False
        else:
            return False

