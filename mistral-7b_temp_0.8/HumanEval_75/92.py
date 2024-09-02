
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    lst = []
    for i in range(3,a,2):
        if a%i == 0:
            lst.append(i)

    if len(lst) == 2:
        return True
    return False
