
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(n):
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    # v = 2 * 3 * 5
    # x = 3 * 5 * 7
    # y = 2 * 5 * 7
    # z = 2 * 3 * 7
    # c = 2 * 3 * 5 * 7
    # n = 2 * 3 * 5 * 7
    # l = 2 * 3 * 5 * 7 * 11
    
    if not is_prime(a):
        return False
    num = 2
    while a > 1:
        if is_prime(a):
            num += 1
        else:
            return False
        a = a/num
    return True
