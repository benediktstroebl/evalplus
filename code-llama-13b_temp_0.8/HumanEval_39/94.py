

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
    fib = [1, 1]
    prime = [2, 3, 5, 7]
    for i in range(n-1):
        fib.append(fib[-1] + fib[-2])
        j = 1
        while True:
            if fib[-1] % prime[j] == 0:
                prime.append(fib[-1])
                break
            elif prime[j] > fib[-1] / 2:
                break
            else:
                j += 1
    return prime[-1]

