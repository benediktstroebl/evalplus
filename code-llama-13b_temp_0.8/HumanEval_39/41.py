

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
    # We'll use a while loop here
    if n <= 0:
        return None

    # init variables
    p_index = 0 # prime index
    f_index = 0 # fibonacci index
    p = 2 # current prime
    f = 0 # current fibonacci
    f_minus2 = 0 # fibonacci before last
    f_minus1 = 1 # fibonacci before before last

    # loop while prime index is less than n
    while p_index < n:
        # calculate next fibonacci
        f = f_minus2 + f_minus1
        # check if it's prime
        if is_prime(p):
            p_index += 1
        # if it is prime, increment prime index
        # and save the value of the current prime
        if p_index == n:
            return p
        # save the current prime as previous prime for next loop
        p = f
        # update fibonacci values for next loop
        f_minus2 = f_minus1
        f_minus1 = f
        f_index += 1

