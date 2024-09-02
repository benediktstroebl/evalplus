
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        for i in range(2, a + 1):
            if a % i == 0:
                x = i
                while x % 2 == 0 or x % 3 == 0:
                    x += 1
                    if a == x:
                        return True
    return False
