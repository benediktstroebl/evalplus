
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_divide = True
    while is_divide:
        a = a / 2
        if not is_prime(a):
            is_divide = False
    return a == 1
