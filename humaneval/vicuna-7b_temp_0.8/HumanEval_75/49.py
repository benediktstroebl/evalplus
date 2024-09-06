
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for num1 in range(2, a):
        for num2 in range(2, a-num1+1):
            if (num1 * num2) == a:
                return True
    return False
