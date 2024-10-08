
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    
    num = 0
    primes = [2]
    
    for i in range(3, 100):
        if a % i == 0:
            num += 1
            primes.append(i)
    
    if num == 3:
        return True
    else:
        return False

