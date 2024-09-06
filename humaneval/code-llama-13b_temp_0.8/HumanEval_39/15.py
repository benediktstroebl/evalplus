

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
    # 0th Fibonacci number == 0 (not prime)
    # 1st Fibonacci number == 1 (prime)
    # 2nd Fibonacci number == 1 (prime)
    # 3rd Fibonacci number == 2 (prime)
    # 4th Fibonacci number == 3 (not prime)
    # 5th Fibonacci number == 5 (prime)
    prime_fib_list = [2, 3]
    last_num = 2
    next_num = 3
    index = 2
    while index < n:
        last_num, next_num = next_num, last_num + next_num
        # This step is very important!
        # We don't want to simply add a new number
        # to the list and assume that it's prime.
        # We check if it's prime.
        if is_prime(next_num):
            prime_fib_list.append(next_num)
            index += 1
    return prime_fib_list[n-1]

