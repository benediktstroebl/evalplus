
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    p1 = 2
    p2 = 3
    p3 = 5
    while p2 < a:
        p2 = 6 - p2
    while p3 < a:
        p3 = 6 - p3
    if p1 == a or p2 == a or p3 == a:
        return False
    for i in range(a - 1):
        if (a % i) == 0:
            return False
    return True
