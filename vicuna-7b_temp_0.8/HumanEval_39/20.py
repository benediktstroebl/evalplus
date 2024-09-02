

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
    # Check if n is a prime number
    if n % 2 != 0:
        return 2
    elif n % 3 == 0:
        return 1
    else:
        # Check if n-1 is prime
        if not is_prime(n-1):
            return n-1
        else:
            # Check if n is a Fibonacci number
            if n == fibonacci(n-1):
                return fibonacci(n)
            else:
                # Check if n is a prime number
                if n > 2:
                    for i in range(2, int(n**0.5) + 1):
                        if not is_prime(n - i):
                            return n
                        else:
                            break
                else:
                    # If n is less than 3, then it's the first Fibonacci number
                    return n