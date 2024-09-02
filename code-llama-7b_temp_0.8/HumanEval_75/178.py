
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # 2 < a < 100
    # 3 < sqrt(a) < 10
    # b < a / b < 33.33
    # c < a / b / c < 11.11

    # Check if number is prime
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in range(2, int(a**(1/3)) + 1):
        if a % i == 0:
            j = a // i
            if is_prime(i) and is_prime(j):
                return True
    return False
