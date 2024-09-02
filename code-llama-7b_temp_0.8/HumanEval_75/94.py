
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check the primes between 2 and 20
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    # Set a flag to true
    result = True
    # Iterate in the list
    for prime in primes:
        # Check if the prime divides the given number
        if a % prime == 0:
            # Divide the given number by the prime number
            a = a/prime
        else:
            # If the number is not divisible, set the flag to false
            result = False
    return result

