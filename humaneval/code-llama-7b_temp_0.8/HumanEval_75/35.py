
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime = [2, 3, 5]

    for i in prime:
        while a % i == 0:
            a = a / i
    return True if a == 1 else False
