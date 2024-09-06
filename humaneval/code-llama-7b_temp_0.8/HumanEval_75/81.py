
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Make a list with all prime numbers up to 10
    primes = [2, 3, 5]
    # start with 2 as the prime number
    prime = 2
    # Loop from 2 to a and append prime numbers to the list
    while prime < a:
        # Let's test if a is divisible by our prime number
        if a % prime == 0:
            # If so, append the prime number to the list
            primes.append(prime)
            # And update a
            a /= prime
        else:
            # If not, just increment our prime number
            prime += 1

    # If a is not divisible by any of the prime numbers
    if a > 1:
        primes.append(a)

    # Check if the product of our prime numbers is equal to the initial number
    return product(primes) == a
