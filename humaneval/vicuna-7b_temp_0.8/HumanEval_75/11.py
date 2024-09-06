
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def check_n_p(n, p):
        if n % p == 0:
            return False
        for i in range(1, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    p1 = 3
    p2 = 5
    while p1 < 100 and p2 < 100:
        if check_n_p(p1, p2):
            p3 = (p1 * p2)
            if check_n_p(p3, p1) and check_n_p(p3, p2):
                return True
        p1 += 2
        p2 += 2
    return False
