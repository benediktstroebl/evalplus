
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if not isinstance(a, int):
        raise TypeError('a must be int')
    if a < 1 or a > 99:
        raise ValueError('a must be between 1 and 100')
    res = 2
    for i in range(2, a//2 + 1):
        if a % i == 0:
            res += 1
    if res == 2:
        return True
    else:
        return False

