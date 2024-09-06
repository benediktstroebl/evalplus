
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

    n_primes = 0
    primes = find_primes(n)

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for prim in primes:
        # only increments the counter if it's prime
        if is_prime(prim):
            n_primes += 1
        if n_primes == n:
            return prim

    class Solution(object):
        def count_up_to(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            if n < 2: return []

            primes = find_primes(n)
            n_primes = len(primes)

            i = 0
            ans = []
            while n_primes > 0:
                if len(ans) >= n: break
                if primes[i] > n: break
                ans.append(primes[i])
                i += 1
                n_primes -= 1
            return ans
