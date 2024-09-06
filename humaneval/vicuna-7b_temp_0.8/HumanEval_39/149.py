

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
    # check that n is not negative
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # check that n is not too large
    if n > 30:
        raise ValueError("n must be less than 31")
    
    # compute the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    
    # check if n-th Fibonacci number is prime
    if n > a:
        for p in range(b, n+1):
            if (n-a) % p == 0:
                return None
        return a
    
    # if n-th Fibonacci number is prime, then n is also prime
    return a

if __name__ == "__main__":
    # example usage
    for i in range(1, 11):
        if prime_fib(i) is not None:
            print(i, "is prime")
    else:
        print("No Fibonacci numbers are prime")