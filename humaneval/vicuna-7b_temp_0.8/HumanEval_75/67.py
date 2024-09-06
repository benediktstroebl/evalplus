
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(x):
        if x == 2:
            return True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_multiple_of_3(x):
        return 3 in [int(x ** 2) % 100 for x in range(1, int(x ** 0.5) + 1)]

    def is_multiple_of_5(x):
        return 5 in [int(x ** 2) % 100 for x in range(1, int(x ** 0.5) + 1)]

    def is_multiple_of_both(x):
        return x == 3 or x == 5

    def is_number_of_3_factors(x):
        factors = set()
        for i in range(int(x ** 0.5) + 1):
            factors.add(i)
        for i in factors:
            for j in range(i + 1, int(x ** 0.5) + 1):
                if x % i == 0 and x % j == 0:
                    return False
        return True

    def is_3_prime_factors(x):
        for i in range(int(x ** 0.5) + 1):
            if is_prime(i):
                for j in range(i + 1, int(x ** 0.5) + 1):
                    if is_prime(j) and is_multiple_of_3(j) and is_multiple_of_3(i) and is_multiple_of_both(x):
                        return True
        return False

    return is_3_prime_factors(a)
