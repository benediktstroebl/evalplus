

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
    # Your code goes here!
    fib = [2, 3]
    index = 0
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
        index += 1

    # Checking if fib[index] is a prime
    prime = True
    if fib[index] == 2:
        prime = True
    else:
        for i in range(2, fib[index]):
            if fib[index] % i == 0:
                prime = False
    return fib[index] if prime else -1

