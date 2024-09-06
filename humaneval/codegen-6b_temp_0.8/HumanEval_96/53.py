
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
    else:
        i = 0
        primes = [2]
        for i in range(3, n+1):
            j = 0
            while primes[j]*primes[j] <= i:
                if i % primes[j] == 0:
                    break
                j += 1
            else:
                primes.append(i)
        return primes

