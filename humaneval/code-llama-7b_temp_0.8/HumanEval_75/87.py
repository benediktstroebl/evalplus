
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # 1- find 3 prime numbers p, q, r
    # 2- make sure that (a) = p * q * r
    # 3- return True if 3 prime numbers p, q, r exist

    #1- find 3 prime numbers p, q, r
    #2- make sure that (a) = p * q * r
    #3- return True if 3 prime numbers p, q, r exist
    # init primes list
    primes = []
    # init first prime
    first_prime = 2
    # check if first_prime is a prime
    if is_prime(first_prime):
        primes.append(first_prime)
    # init second prime
    second_prime = 3
    # check if second_prime is a prime
    if is_prime(second_prime):
        primes.append(second_prime)
    # init third prime
    third_prime = 5
    # check if third_prime is a prime
    if is_prime(third_prime):
        primes.append(third_prime)

    print("primes are:",primes)

    # init multiplier
    multi = 1
    for prime in primes:
        multi *= prime
    print(multi)
    if multi == a:
        return True
    else:
        return False
