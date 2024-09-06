
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(number):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    for i in range(2, 100):
        if is_prime(i):
            for j in range(2, 100):
                if is_prime(j):
                    for k in range(2, 100):
                        if is_prime(k):
                            if i * j * k == a:
                                return True
    return False

