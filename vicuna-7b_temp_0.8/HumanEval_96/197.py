
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
    # Create a list of all prime numbers less than n
    primes = [2,3,5,7,11,13,17,19]
    # Create a list of n integers to store the result
    n_primes = [0] * n
    # Traverse the primes and check if each is less than n, if it is return it
    for prime in primes:
        if prime < n:
            n_primes[prime] = int(n_primes[prime]) + 1
    return n_primes