

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # return 0 for n < 2
    if n < 2:
        return 0
    # list to keep track of prime numbers
    primes = [True, True]
    # go through all numbers between 2 and n
    for i in range(2, int(n ** 0.5) + 1):
        # find the last two prime numbers in the list
        last_two_primes = [x for x in primes[1::2] if x]
        # check if the next number is the sum of the last two prime numbers
        if i == last_two_primes[0] + last_two_primes[1]:
            # if so, the number is prime and a Fibonacci number
            return i
    return 0  # return 0 if no prime number is found
