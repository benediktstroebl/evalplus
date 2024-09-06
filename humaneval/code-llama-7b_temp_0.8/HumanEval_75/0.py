
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2,101):
        count = 0
        for j in range(2,i):
            if i % j == 0:
                count += 1
                if count > 2:
                    return False
        if count == 2:
            return True
    return False
