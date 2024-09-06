
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        x = a
        for i in range(3, int(a/3) + 1):
            if x % i == 0:
                n = x // i
                if is_prime(n):
                    return is_prime(n) and is_prime(x // n) and is_prime(n // x)
        return False
    else:
        return "Error, the number must be less then 100"
    

