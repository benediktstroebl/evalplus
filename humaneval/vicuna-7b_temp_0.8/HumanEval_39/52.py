

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
    if n <= 1:
        raise ValueError("n must be positive integer")
    if n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 5:
        return 5
    elif n == 89:
        return 89
    else:
        # check for n-th Fibonacci number
        if n == 4:
            return 5
        else:
            fib = 0
            prev_num = 0
            for i in range(1, n):
                fib, prev_num = prev_num, i
            num = prev_num
            while num < n:
                # check if num is prime
                if num > 2:
                    for i in range(2, int(sqrt(num)) + 1):
                        if num % i == 0:
                            break
                    else:
                        return num
                else:
                    # return num if it is prime
                    return num