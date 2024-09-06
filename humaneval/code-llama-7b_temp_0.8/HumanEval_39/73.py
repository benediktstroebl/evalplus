

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
    if n == 1:
        return 2
    if n == 2:
        return 3

    primes = [2]
    prime_len = 1
    current_num = 3
    while True:
        # print(current_num)
        is_prime = True
        for prime in primes[:prime_len]:
            if current_num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_num)
            prime_len += 1
        if prime_len >= n:
            return current_num

        fib = primes[prime_len-1] + primes[prime_len-2]
        current_num = fib

