
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    number = a
    count = 0
    for x in range(2, number):
        if number % x == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False
