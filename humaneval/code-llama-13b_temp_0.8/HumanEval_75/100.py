
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    # if number is less then 100 then it can be divided by 2,3,5,7,9 or 11
    if a < 100:
        return False
    sqr_a = int(a ** 0.5)
    for i in range(2, sqr_a + 1):
        if a % i == 0 and is_prime(i) and is_prime(int(a / i)):
            return True
    return False
