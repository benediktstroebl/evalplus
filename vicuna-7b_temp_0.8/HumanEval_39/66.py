

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
    d = [0, 1, 1]
    while d[-1] < n:
        d.append(d[-1] + d[d[-2]] % d[-1])
    
    # Check if n is prime
    if n % 2 == 0:
        return 2
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return 2
        
        # n is prime
        digits = str(n)
        while digits[-1] in ["5", "0"]:
            digits = digits[:-1]
        last_digit = digits[-1]
        if last_digit == "5":
            if d[-1] == d[-2] % d[-1] + d[-2] % d[-3] % d[-1]:
                return d[-1]
        else:
            if d[-1] == d[-2] % d[-1] + d[-2] % d[-3] % d[-2]:
                return d[-2]
        # n is not prime
        return 2