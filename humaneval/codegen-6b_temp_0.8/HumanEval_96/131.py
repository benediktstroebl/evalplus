
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
    # elif n == 1:
    #     return [2]

    limit = n
    primes = [True] * limit
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            # mark multiples of i as not prime
            for j in range(i * i, limit, i):
                primes[j] = False

    # create a list of primes up to n
    return [i for i, is_prime in enumerate(primes) if is_prime]

