
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_prime = [True] * 100
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p <= 100:
        if is_prime[p]:
            k = p * 2
            while k <= 100:
                is_prime[k] = False
                k += p
        p += 1
    
    for i in range(2, 100):
        if is_prime[i]:
            if a % i == 0:
                a = a // i
                if is_prime[a]:
                    return True
    return False
