

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
    def prime_numbers(num):
        """
        prime_numbers returns list of prime numbers up to n.
        >>> prime_numbers(20)
        [1, 2, 3, 5, 7, 11, 13, 17, 19]
        """
        primes = [1, 2]
        num_primes = 2
        prime = primes[-1] + 2
        if num < 3:
            return primes[:num]
        else:
            while num_primes < num:
                prime += 2
                if all([prime % p for p in range(3, int(prime ** 0.5) + 1, 2)]):
                    num_primes += 1
                    primes.append(prime)
        return primes

    def fibonacci(num):
        """
        fibonacci returns Fibonacci numbers up to n.
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
        """
        fib_seq = [0, 1]
        if num < 2:
            return fib_seq[:num]
        else:
            while len(fib_seq) < num:
                fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

    prime_fibs = [x for x in prime_numbers(2*n) if x in fibonacci(n)]
    return prime_fibs[n-1]

