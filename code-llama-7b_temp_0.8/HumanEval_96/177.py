
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
    # 1st solution, time complexity O(n), space complexity O(1)
    # primes = []
    # for i in range(2, n + 1):
    #     is_prime = True
    #     for j in range(2, i):
    #         if i % j == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         primes.append(i)
    # return primes
    # 2nd solution, time complexity O(n), space complexity O(n)
    # primes = [False, False, True] + [True] * (n - 2)
    # for i in range(2, n + 1):
    #     if primes[i]:
    #         for j in range(i * i, n + 1, i):
    #             primes[j] = False
    # return [i for i in range(n) if primes[i]]
    # 3rd solution, time complexity O(n), space complexity O(1)
    primes = []
    if n <= 1:
        return primes
    is_prime = [True] * n
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n, i):
                is_prime[j] = False
    return primes

