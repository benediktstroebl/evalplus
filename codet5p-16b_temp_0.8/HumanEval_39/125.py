

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

    primes = []
    fib = [1,1]
    index = 1
    while index < n:
        next_num = fib[0] + fib[1]
        if next_num % 2 == 0:
            fib[0] = fib[1]
            fib[1] = next_num
            continue
        else:
            is_prime = True
            for prime in primes:
                if prime > fib[1]:
                    break
                if fib[1] % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(fib[1])
                index += 1
            fib[0] = fib[1]
            fib[1] = next_num

    return fib[1]


