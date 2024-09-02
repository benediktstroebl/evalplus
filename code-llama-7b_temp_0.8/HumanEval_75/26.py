
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    if a < 100:
        if is_prime(a):
            return False
        for i in range(1, a):
            if a % i == 0:
                if is_prime(i):
                    if a / i == i:
                        return True
        return False
