
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n_factor = 2
    while n_factor < 10:
        if n_factor == 2 or n_factor == 3 or n_factor == 5:
            n_factor += 1
            continue
        if is_prime(n_factor) == True:
            while a % n_factor == 0:
                a = a/n_factor
                n_factor += 1
        else:
            n_factor += 1
    return a == 1
