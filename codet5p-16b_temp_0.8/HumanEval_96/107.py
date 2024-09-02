
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

    primes = [2,3,5,7,11,13,17]
    if n <= 7:
        return primes[0:n]
    if n <= 13:
        return primes[0:n-1]
    if n <= 17:
        return primes[0:n-2]
    if n <= 19:
        return primes[0:n-3]
    if n <= 23:
        return primes[0:n-4]
    if n <= 29:
        return primes[0:n-5]
    if n <= 31:
        return primes[0:n-6]
    if n <= 37:
        return primes[0:n-7]
    if n <= 41:
        return primes[0:n-8]
    if n <= 43:
        return primes[0:n-9]
    if n <= 47:
        return primes[0:n-10]
    if n <= 53:
        return primes[0:n-11]
    if n <= 59:
        return pr
