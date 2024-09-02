
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    limit = 100
    a_sqrt = int(math.sqrt(a))
    D = {}
    for x in range(2, a_sqrt + 1):
        for y in range(2, a_sqrt + 1):
            p = x * y
            if p <= limit:
                D[p] = 1
            else:
                break
    if a in D:
        return False
    else:
        return True




