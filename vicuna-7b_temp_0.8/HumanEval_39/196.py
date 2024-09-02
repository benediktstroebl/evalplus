

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
    # 2 is the first Fibonacci number and it's prime
    if n == 1:
        return 2
    # 3 is the second Fibonacci number
    elif n == 2:
        return 3
    # check if the next number in the sequence is prime
    elif n % 2 == 0:
        return False
    else:
        # find the next Fibonacci number
        fib_num = (2 * (n - 1)) + 1
        # check if it's prime
        if fib_num > 10000:
            # if the number is greater than 10000, there's a high chance it's prime
            return True
        else:
            # if the number is less than 10000, check it manually
            for i in range(2, fib_num):
                if fib_num % i == 0:
                    return False
            return True