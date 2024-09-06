
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        """
        Check if a number is prime
        :param n: the number to check
        :return: True if n is prime, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        p1, p2, p3 = 2, 3, 5
        while (p1 <= a):
            while (p2 <= a):
                while (p3 <= a):
                    if is_prime(p1) and is_prime(p2) and is_prime(p3) and a % (p1 * p2 * p3) == 0:
                        return True
                    p1 += 2
                    p2 += 2
                    p3 += 2
            p1 = 4
            p2 = 4
            p3 = 3
        return False

    return is_multiply_prime(a)
