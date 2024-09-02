
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # TODO: Write code here
    primes = []
    for num in range(2, a):
        if is_prime(num):
            primes.append(num)

    if len(primes) != 3:
        return False

    for prime in primes:
        if a % prime != 0:
            return False

    return True
