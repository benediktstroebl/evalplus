
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if not isinstance(a,int):
        return False
    if a > 100:
        return False
    if a < 2:
        return False
    elif a == 2:
        return True
    for i in range(2, a):
        if a%i == 0:
            return False
    for i in range(2,a):
        for j in range(2,a):
            if i*j == a:
                if is_prime(i) and is_prime(j):
                    return True
    return False
