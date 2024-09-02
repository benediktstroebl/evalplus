
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Use the Sieve of Eratosthenes to find all prime numbers less than a
    sieve = [True] * (a + 1)
    for p in range(2, int(a ** 0.5) + 1):
        if p > a:
            break
        if sieve[p]:
            for i in range(p ** 2, int(a ** 0.5) + 1, p):
                sieve[i] = False
    # Check if the number is a product of 3 prime numbers
    for i in range(3):
        for j in range(3, a + 1):
            if (a % (i, j)) == 0:
                return False
    return True