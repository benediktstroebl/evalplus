

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # use a simple sieve to check if a number is prime
    # note: this is a very inefficient method
    # for large numbers
    
    # we can use a sieve of Eratosthenes to find prime numbers
    # efficiently
    # first, we write the numbers from 2 to the square root of n in an array
    # then, we can use the following algorithm:
    # for each number in the array, if it is prime, we mark it in the sieve
    # by setting its corresponding bit in the sieve array to 1
    # we can then use the sieve to determine if a given number is prime
    # by checking if its corresponding bit in the sieve is 1 or 0

    # in this example, we will use a simple sieve to check if a number is prime
    # it is not efficient for large numbers
    # but it is easy to understand and implement

    # check the first two conditions: n must be an integer and n > 1
    if not (n % 1 == 0 and n % 2 == 0):
        return False

    # we will use a list of numbers to store the prime numbers
    # we will add 2 to the list of numbers because the first number in the sieve is 3, not 2
    primes = [2]

    # we will use a variable to store the last number in the sieve
    last = 2

    # we will use a variable to store the current number
    current = 3

    # while the current number is less than the square root of n
    while current <= math.sqrt(n):
        # if the current number is prime, add it to the list
        if current % 2 == 0:
            # we can use the current number as the last number in the sieve
            last = current
            # we will add 2 to the current number, so that we can check if the next number is prime
            current += 2
        else:
            # we can use the current number to check if the next number is prime
            # if the next number is prime, we can use the current number as the last number in the sieve
            if current % current == 0:
                #
