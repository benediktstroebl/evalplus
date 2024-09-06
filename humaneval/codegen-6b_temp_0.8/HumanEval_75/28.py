
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i = 2
    while i < a:
        if is_prime(i):
            j = i
            k = a / j
            while j < k:
                if is_prime(k) and is_prime(j):
                    if a % (j * k) == 0:
                        return False
                j += 1
                k = a / j
        i += 1
    return True
