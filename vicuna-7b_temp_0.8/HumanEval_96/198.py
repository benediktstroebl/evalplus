
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
    sieve = [True] * (n+1)
    sieve[0] = False
    prime_numbers = [2]
    for p in sieve[2:]:
        while p * p <= n:
            if sieve[p]:
                for i in range(p*p,n+1,p+1):
                    sieve[i] = False
    return prime_numbers
