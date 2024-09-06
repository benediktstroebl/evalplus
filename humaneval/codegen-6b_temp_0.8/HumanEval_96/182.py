
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
    
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    
    result = []
    for x in range(2,n+1,1):
        if primes[x]:
            result.append(x)
            primes[x*2:n+1:x] = [False] * len(primes[x*2:n+1:x])
    
    return result
