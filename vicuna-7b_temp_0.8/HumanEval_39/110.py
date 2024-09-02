

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
    if n < 0:
        raise ValueError("n should be a positive integer.")
    
    def fib(x):
        a, b = 0, 1
        while a < x:
            a, b = b, a + b
        return b
    
    def is_prime(x):
        if x <= 1:
            return True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if fib(i) % i == 0:
            return None
        if is_prime(i):
            if fib(i) % fib(i - 1) == 0:
                return None
            primes = [i]
            while True:
                a = i + 1
                while a < n and (a, fib(a)) not in primes:
                    if fib(a) % fib(a - 1) == 0:
                        return None
                    primes.append((a, fib(a)))
                    a += 1
                if a > n:
                    break
            return int(primes[-1][0])
    
    return None