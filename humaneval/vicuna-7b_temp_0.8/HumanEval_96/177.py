
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
    # use a sieve of eratosthenes algorithm to find prime numbers less than n
    sieve = [True] * (n+1)
    for p in range(2,n+1):
        if sieve[p]:
            for i in range(p*p,n+1,p):
                sieve[i] = False
    # filter the prime numbers that are less than n
    prime_numbers = [p for p in range(2,n+1) if sieve[p]]
    return prime_numbers
