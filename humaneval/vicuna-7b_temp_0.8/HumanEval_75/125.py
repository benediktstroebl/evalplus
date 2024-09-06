
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for num in range(2, int(a**0.5)+1):
        for i in range(num, a-1, 2):
            for j in range(num, a-1, 2):
                if (a % (i*j)) == 0:
                    return False
        if a % 3 == 0 and a % 5 == 0:
            return False
    return True