
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_prime_3(n):
        if n == 2:
            return True
        if n == 3:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_prime_5(n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n == 5:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_prime_all(n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n == 5:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    is_prime_test = is_prime(a)
    if is_prime_test == True:
        for i in range(2, int(a**0.5) + 1):
            if is_prime_3(i) == False:
                for j in range(2, int(i**0.5) + 1):
                    if is_prime_5(j) == False:
                        for k in range(2, int(j**0.5) + 1):
                            if is_prime_all(k) == False:
                                return True
    else:
        for i in range(2, int(a**0.5) + 1):
            if is_prime_5(i) == False:
                for j in range(2, int(i**0.5) + 1):
                    if is
