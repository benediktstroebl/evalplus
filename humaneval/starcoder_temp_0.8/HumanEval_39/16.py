

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
    # base case
    if n == 1:
        return 2
    if n == 2:
        return 3
    
    # case where the given number is Fibonacci number
    f1 = 0
    f2 = 1
    # base case
    if n == 3:
        return 5
    
    for i in range(3, n + 1):
        f1, f2 = f2, f1 + f2
        
    prime_list = [2]
    prime_list.extend(range(3, f2 + 1, 2))
    for i in range(f2 + 1, n + 1):
        # assume it's prime number
        isPrime = True
        for j in prime_list:
            if i % j == 0 and j!= i:
                isPrime = False
                break
        if isPrime:
            return i
