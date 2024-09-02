
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # initialize a list of prime numbers less than a
    primes = [True, True, True, True, True, True, True, True, True, True, True, True, True]
    primes[-1] = is_prime(a-1)
    
    if a == 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, int(a/2)+1):
            if a % i == 0:
                break
        else:
            for j in range(2, int(a/2)+1):
                if (j*j) % i == 0:
                    break
        if all(primes[i] for i in range(2, int(a/2)+1)):
            return True
        else:
            return False
