
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        res = True
        prime_list = []
        x = 2
        while res:
            if x < a:
                if a % x == 0:
                    a //= x
                    prime_list.append(x)
                    x = 2
                else:
                    x += 1
            else:
                res = False
        if len(prime_list) == 3:
            return True
        else:
            return False
    return False

