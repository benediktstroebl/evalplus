
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    x = 3
    result = []
    while x <= a:
        if a % x == 0:
            result.append(x)
            a = a / x
        else:
            x += 1
    if len(result) == 2:
        return False
    if a == 1:
        return True

