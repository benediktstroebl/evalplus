
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Predicate
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True
    # Main body
    def is_multiply(num):
        if num % 2 == 0:
            return False
        for i in range(3, int(pow(num, 0.5)) + 1, 2):
            if num % i == 0:
                return False
        return True
    for i in range(3, 100, 2):
        if is_prime(i) and is_multiply(i):
            for j in range(3, int(pow(i, 0.5)) + 1, 2):
                if i % j == 0 and is_prime(j):
                    return False
    return True
