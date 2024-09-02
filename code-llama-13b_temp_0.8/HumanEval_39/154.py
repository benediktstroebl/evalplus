

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

    # backward
    # memo[n] is the n-th prime Fibonacci number
    memo = [-1] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    # last_Fib[i] is the last Fibonacci number we have seen
    # so the next Fibonacci number is either last_Fib[i] + last_Fib[i-1], or last_Fib[i-1] + last_Fib[i-2]
    last_Fib = [-1] * (n + 1)
    last_Fib[1] = 1
    last_Fib[2] = 1
    # last_Prime[i] is the last prime we have seen
    last_Prime = [-1] * (n + 1)
    last_Prime[0] = 1
    last_Prime[1] = 2

    # find prime Fibonacci numbers and store them in memo and last_Fib
    i = 2
    while True:
        # next Fibonacci number is either last_Fib[i] + last_Fib[i-1], or last_Fib[i-1] + last_Fib[i-2]
        next_Fib = last_Fib[i] + last_Fib[i - 1]
        # check if next Fibonacci number is prime
        is_Prime = True
        for j in range(2, int(next_Fib ** 0.5 + 1)):
            if next_Fib % j == 0:
                is_Prime = False
                break
        if is_Prime:
            last_Prime[i + 1] = last_Fib[i]
            memo[i + 1] = last_Prime[i]
            last_Fib[i + 1] = next_Fib
            # check if the length of prime Fibonacci numbers we have found is enough
            if len(memo) - 1 >= n:
                return memo[n]
            i +=
