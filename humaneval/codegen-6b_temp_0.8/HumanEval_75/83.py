
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    is_multiply = False

    for i in range(a):
        if i * 9 == a:
            is_multiply = True
            break
        elif i * 3 == a:
            is_multiply = True
            break

    return is_multiply

