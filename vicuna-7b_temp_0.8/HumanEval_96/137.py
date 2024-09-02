
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
    if n < 2:
        return []
    #check for 2, because it's not considered a prime number
    if n == 2:
        return [2]
    sieve_of_eratosthenes = [True] * (n+1)
    for i in range(1, n+1):
        for j in range(i*i, n+1, i):
            sieve_of_eratosthenes[j] = False
    primes = []
    for i in range(2, n+1):
        if sieve_of_eratosthenes[i]:
            primes.append(i)
    return primes
