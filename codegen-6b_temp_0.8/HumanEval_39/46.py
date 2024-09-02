

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    fib = [0, 1]
    for i in range(1, n):
        fib.append(fib[-1] + fib[-2])
    ans = 0
    while True:
        j = 0
        while fib[j] * fib[j + 1] < n:
            j += 1
        if fib[j] * fib[j + 1] == n:
            ans = n
            break
        else:
            n -= fib[j] * fib[j + 1]
    # while True:
    #     prime = True
    #     if (n % fib[0]) == 0:
    #         prime = False
    #         break
    #     j = 1
    #     while fib[j] * fib[j] < n:
    #         if (fib[j] * fib[j]) == n:
    #             prime = False
    #             break
    #         j += 1
    #     if prime:
    #         ans = n
    #         break
    #     n -= fib[j]
    print(ans)
    return ans

