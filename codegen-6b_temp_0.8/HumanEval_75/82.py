
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Using Sieve of Eratosthenes, O(n log n)
    sieve = [True] * (a+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.ceil(math.sqrt(a)))+1):
        if sieve[i]:
            for j in range(i*i, a+1, i):
                sieve[j] = False
    for i in range(3, a+1, 2):
        if sieve[i]:
            return True
    return False
