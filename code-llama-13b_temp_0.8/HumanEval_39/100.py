

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

    fib_list = [1, 1]
    num_list = [2, 3]
    count = 2

    while True:
        fib_list.append(fib_list[count - 1] + fib_list[count - 2])
        if prime_test(fib_list[count]) == True:
            num_list.append(fib_list[count])
            count += 1
            if len(num_list) >= n:
                return num_list[n - 1]
        else:
            count += 1

