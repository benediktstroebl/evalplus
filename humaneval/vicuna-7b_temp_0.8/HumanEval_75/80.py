
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Write a helper function to check if a number is prime
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    # Initialize an empty list to store the prime factors of a
    prime_factors = []

    # Use a for loop to find all the prime factors of a
    for i in range(2, int(a ** 0.5) + 1):
        # If the number is prime, append its factors to the list
        if is_prime(i):
            prime_factors.append(i)

    # Use another for loop to check if all the factors of a are products of 3 primes
    for j in range(1, len(prime_factors)):
        if len(set(prime_factors[:j])) <= 2:
            return True
    return False
