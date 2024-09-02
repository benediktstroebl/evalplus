
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_prime = [True for i in range(1, a + 1)]
    p = [2, 3]
    while len(p) > 0:
        a_temp = a
        while a_temp % p[0] == 0:
            a_temp = a_temp // p[0]
            p = p[:]
            p.append(a_temp % p[0])
        if p[0] > a and p[0] % 2 == 1:
            is_prime = [False for i in range(a_temp, a + 1) if (i % p[0]) == 0]
        if p[0] == a:
            break
    return not any(is_prime)