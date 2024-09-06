
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # function to check if n is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # function to check if n is the product of 3 primes
    def is_product_of_3_primes(n):
        if n < 3:
            return False
        if is_prime(n) != True:
            return False
        p = 2
        while (p * p) <= n:
            if is_prime(n/p) != True:
                return False
            p += 1
        return True

    # check if a is the product of 3 primes
    if is_product_of_3_primes(a) == True:
        return True
    else:
        return False

result = is_multiply_prime(5)
