
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    numbers = [2, 3, 5]
    c = 0
    while a > 0:
        for n in numbers:
            if a % n == 0:
                c += 1
                break
        if c >= 3:
            return True
        else:
            a = a // 10
            c = 0
    return False
