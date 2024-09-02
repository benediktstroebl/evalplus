
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    primes = [2,3,5]
    for i in range(6,a):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    if a % 3 == 0:
        return True
    return False

