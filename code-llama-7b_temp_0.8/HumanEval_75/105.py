
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = 100
    i = 0
    j = 0
    k = 0
    while i < n:
        if i > 1 and not is_prime(i):
            i += 1
            continue
        j = 0
        while j < n:
            if j > 1 and not is_prime(j):
                j += 1
                continue
            k = 0
            while k < n:
                if k > 1 and not is_prime(k):
                    k += 1
                    continue
                if i * j * k == a:
                    return True
                k += 1
            j += 1
        i += 1
    return False

