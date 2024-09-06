
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # NOTE: this function uses the Sieve of Eratosthenes
    # to generate all prime numbers up to a given limit
    # to check if the input number a is a cube of any prime number
    # this will take some time and storage, so be careful!

    # generate all prime numbers up to sqrt(a)
    primes = [2]
    for p in range(3, int(a**0.5)+1, 6):
        if a % p == 0:
            continue
        primes.append(p)
    primes.extend([p**3 for p in primes])

    # check if any of the prime factors of a are equal to the input number a
    for p in primes:
        if p == int(a):
            return True

    # no prime factors found, so a is not a cube
    return False