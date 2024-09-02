
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    #Slow way
    if a % 2 == 0:
        return False
    
    for i in range(3, a, 2):
        if a % i == 0:
            prime_num = 0
            for j in range(3, i, 2):
                if i % j == 0:
                    prime_num += 1
            if prime_num == 2:
                return True
    
    return False

