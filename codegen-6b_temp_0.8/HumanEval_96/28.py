
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
    def count_up_to_rec(n):
        if n == 1:
            return []
        return [n] + count_up_to_rec(n-1)
    prime_count = 0
    start = time.time()
    more_primes = count_up_to_rec(n)
    end = time.time()
    time_elapsed = end - start
    return [len(more_primes), time_elapsed]
