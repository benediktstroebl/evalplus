
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        b = a
        c = 0
        d = 0
        while b != 1:
            for i in range(2, 100):
                if b % i == 0:
                    d = i
                    b = b / i
            if b == 1:
                c = d
                break
        if c == 3:
            return True
    else:
        return False
