
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    
    is_multiply_prime_true = False
    for i in range(2, int(a/2)):
        is_prime = True
        for j in range(2, int(i/2)):
            if i % j == 0:
                is_prime = False
        if is_prime:
            for k in range(2, int(a/i)):
                if i*k == a:
                    is_multiply_prime_true = True
                    break
    return is_multiply_prime_true
    
    
