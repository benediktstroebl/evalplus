
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    a = a-1
    if a % 2 == 0:
        return False
    i = 3
    while a % i!= 0:
        i = i + 2
    if i == a:
        return True
    else:
        return False
    pass

