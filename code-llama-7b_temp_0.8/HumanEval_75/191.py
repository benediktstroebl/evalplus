
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    l = []
    for i in range(2,a):
        if a%i == 0:
            l.append(i)
    if len(l) < 3:
        return False
    else:
        for i in l:
            if is_prime(i) == False:
                return False
            else:
                return True
