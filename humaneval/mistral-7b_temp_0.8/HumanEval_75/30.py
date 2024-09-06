
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    list_a = []
    for i in range(1, 10):
        if a % i == 0:
            list_a.append(i)
    if len(list_a) == 3:
        for i in range(2, 10):
            if i in list_a:
                return True
    return False

