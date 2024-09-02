

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
    # check if n is prime
    if not n % 2 == 0:
        return 0
    if not n % 3 == 0:
        return 1

    # check if n is a Fibonacci number
    if n == 0 or n == 1:
        return n

    # check if n is prime
    # ...
    #
    # We can use Sieve of Eratosthenes algorithm to efficiently find prime numbers
    # ...

    # check if n is prime
    # ...
    #
    # In this case, we can use a dictionary to store all prime numbers up to n
    # ...

    # check if n is prime
    # ...
    #
    # In this case, we can use a list of all prime numbers up to n
    # ...

    # check if n is prime
    # ...
    #
    # In this case, we can use a list comprehension to check if n is prime
    # ...

    # check if n is prime
    # ...
    #
    # We can use a for loop to check if n is prime
    # ...

    # check if n is prime
    # ...
    #
    # In this case, we can use a recursive function to check if n is prime
    # ...

    return 0

if __name__ == "__main__":
    for n in range(1, 20):
        if prime_fib(n) == 0:
            print(n)