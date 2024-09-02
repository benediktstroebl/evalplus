

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
    # Your code here
    count = 0
    prime_list = [2, 3]
    fib_list = [1, 1]
    while count != n:
        new_num = fib_list[-1] + fib_list[-2]
        fib_list.append(new_num)
        if prime(new_num):
            prime_list.append(new_num)
            count += 1
    return prime_list[-1]

