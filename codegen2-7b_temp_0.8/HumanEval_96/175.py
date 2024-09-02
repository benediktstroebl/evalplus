
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
    if n == 0:
        return []
    if n < 0:
        raise Exception('count_up_to should be called with a non-negative number')
    primes = [2, 3]
    i = 5
    while i <= n:
        if is_prime(i):
            primes.append(i)
        i += 2
        if len(primes) >= n:
            return primes
    return pr
