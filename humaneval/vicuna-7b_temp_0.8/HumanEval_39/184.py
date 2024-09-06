

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
    if n < 2:
        raise ValueError("Invalid input")
    
    fib_list = [0, 1]
    n_list = [0, 1, 2]
    prime_list = [True] * (n // 2)
    
    for i in range(n // 2, n):
        for j in range(2, i):
            if fib_list[i - j] > n_list[j]:
                break
        else:
            prime_list[i] = False
        
    fib_num = fib_list[n - 2]
    prime = True
    
    for i in range(n // 2, n):
        if prime_list[i]:
            prime = False
        elif fib_num % prime_list[i - 1] != 0:
            prime = False
        
    return prime_list[n - 1]