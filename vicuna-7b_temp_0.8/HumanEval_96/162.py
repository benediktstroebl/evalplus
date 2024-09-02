
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
    #print n
    if n == 0:
        return []
    if n == 1:
        return [2]
    if n in [2,3]:
        return [n]
    primes = [2]
    while len(primes) < n:
        for p in primes:
            for i in range(2, p+1):
                if (p*i) % n == 0:
                    break
            else:
                primes.append(p)
    return primes[:n]
