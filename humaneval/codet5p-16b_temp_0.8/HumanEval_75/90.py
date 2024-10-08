
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    i = 3
    while(i * i <= a):
        if a % i == 0:
            j = a // i
            if is_prime(i) and is_prime(j):
                return True
            else:
                return False
        i += 2
    return False
