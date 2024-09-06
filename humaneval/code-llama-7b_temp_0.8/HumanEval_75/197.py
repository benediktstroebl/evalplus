
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Make a list of prime numbers that are less than 30 
    primes = [2, 3, 5]
    for i in range(7, 99):
        prime = True
        for prime_num in primes:
            if i % prime_num == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    print(primes)
    is_product = False
    for prime_1 in primes:
        for prime_2 in primes:
            for prime_3 in primes:
                if prime_1 * prime_2 * prime_3 == a:
                    is_product = True
                    break
            if is_product:
                break
        if is_product:
            break
    return is_product

