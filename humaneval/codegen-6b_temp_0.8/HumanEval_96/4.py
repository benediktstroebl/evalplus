
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("1st argument must be a positive integer")

    # initialize primes list
    primes = []

    # if n is 0, method should return empty list []
    if n == 1:
        return primes

    # if n is 1, method should return [2]
    if n == 2:
        return primes + [2]

    # for n > 2, define some boolean variable is_prime which is initially set to True
    is_prime = True
    i = 2
    # for i in [2,3,5,...,n]:
    while i <= n:
        # if i is divisible by any number from 2 to n-1, set is_prime to False
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        # if is_prime is True, append i to the primes list
        # note that we use append() instead of += to append to a list
        if is_prime:
            primes.append(i)
        i += 1
        is_prime = True

    return primes

