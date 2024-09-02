
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        if a == 1:
            return False
        prime_nums = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in prime_nums:
            if a % i == 0:
                return True
        return False
    return "a is bigger then 100"
