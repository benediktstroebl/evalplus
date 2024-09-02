
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
    if n <= 1:
        return []
    prime = [True for i in range(n)]
    p = 2
    while p * p < n:
        if prime[p]:
            for i in range(p * 2, n, p):
                prime[i] = False
        p += 1
    primes = []
    for idx, p in enumerate(prime):
        if p and idx > 1:
            primes.append(idx)
    return primes
