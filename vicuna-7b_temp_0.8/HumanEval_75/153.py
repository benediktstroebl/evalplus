
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def _is_multiply_prime(a):
        """
        This function uses the Sieve of Eratosthenes algorithm to check if a number is the product of 3 prime numbers.
        """
        # Use the Sieve of Eratosthenes algorithm to generate the list of prime numbers less than a
        if a <= 100:
            sieve = [True] * (a + 1)
            for i in range(2, int(a**0.5) + 1):
                if a % i == 0:
                    for j in range(i**2, int(a**0.5) + 1, i):
                        sieve[j] = False
            # Compare the remaining numbers in the sieve to the input number and return true if there is no match
            for i in range(a + 1, len(sieve)):
                if sieve[i] == True:
                    if is_prime(a * sieve[i]):
                        return True
        return False

    return _is_multiply_prime(a)
