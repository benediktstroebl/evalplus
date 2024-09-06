
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a > 100:
        return False
    num_list = [True for x in range(a + 1)]
    for i in xrange(3, a + 1, 2):
        if not num_list[i]:
            continue
        for j in xrange(i + i, a + 1, i):
            num_list[j] = False
    return num_list[a]
