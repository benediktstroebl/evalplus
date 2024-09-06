
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
    # all numbers are potential primes until proven otherwise
    primes = [i for i in range(2, n)]
    # start from 2
    num = 2
    # while there are unchecked primes left
    while num <= n:
        for i in range(num+1, n):
            if i in primes and i % num == 0:
                primes.remove(i)
        num += 1
    return primes
