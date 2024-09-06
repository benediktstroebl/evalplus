
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(number):
        if number < 2:
            return False
        i = 2
        while i*i <= number:
            if number % i == 0:
                return False
            i += 1
        return True
    
    n = a
    i = 1
    while i < 4:
        if not is_prime(n):
            return False
        n = n / 2
        i += 1
    return True
