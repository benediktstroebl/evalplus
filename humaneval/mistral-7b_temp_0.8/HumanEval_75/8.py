
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def check_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, n//2, 2):
            if n % i == 0:
                return False
        return True

    a = list(str(a))
    n = int(a[0])
    n1 = int(a[1])
    n2 = int(a[2])
    if check_prime(n) and check_prime(n1) and check_prime(n2):
        return True
    else:
        return False
