
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_is_prime = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            a_is_prime = False
            break
    if a_is_prime:
        for i in range(2, int(a ** 0.5) + 1):
            for j in range(i + 1, int(a ** 0.5) + 1):
                if (a % (i * j)) == 0:
                    a_is_prime = False
                    break
    return a_is_prime
