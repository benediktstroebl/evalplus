
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # def is_prime(x):
    #     """Check if integer x is a prime number."""
    #     i = 2
    #     while i * i <= x:
    #         if x % i == 0:
    #             return False
    #         i += 1
    #     return True

    # for i in range(1, 100):
    #     for j in range(1, 100):
    #         for k in range(1, 100):
    #             if a == i * j * k and is_prime(i) and is_prime(j) and is_prime(k):
    #                 return True
    # return False

    # from math import sqrt
    # n = 100
    # primes = [True for i in range(n)]
    # p = 2
    # while p * p < n:
    #     if primes[p] == True:
    #
    #         for i in range(p * p, n, p):
    #             primes[i] = False
    #     p += 1
    #
    # for i in range(2, n):
    #     if primes[i] and a % i == 0:
    #         if a / i in primes:
    #             return True
    # return False

    n = 100
    prim_list = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, num)):
            prim_list.append(num)

    for i in range(len(prim_list)):
        for j in range(i, len(prim_list)):
            for k in range(j, len(prim_list)):
                if prim_list[i] * prim_list[j] * prim_list[k] == a:
                    return True
    return False
