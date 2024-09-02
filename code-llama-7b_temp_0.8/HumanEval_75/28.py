
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2, 100):
        j = 2
        k = 2
        while j <= i/2:
            if i%j == 0:
                k = i/j
                j += 1
            elif i%j != 0:
                j = i/k + 1
            if j > i/2:
                break
            elif k <= i/2:
                continue
            else:
                return False
    return True
