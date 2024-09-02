

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
    # Check whether the number is negative. If yes return None.
    if n < 1:
        return None
    # Initial values for Fibonacci sequence
    x_n_2 = 0
    x_n_1 = 1
    # 1st number that is prime
    x_n = 2
    # 2nd number that is prime
    x_n_1_plus = 3
    # counter for number of prime numbers found
    p_count = 1
    # Loop until p_count reaches n
    while p_count < n:
        # Check whether x_n is prime
        prime_flag = True
        for i in range(2, x_n//2 + 1):
            if x_n % i == 0:
                prime_flag = False
                break
        # If x_n is prime increase p_count by 1.
        if prime_flag:
            p_count += 1
        # Calculate next number in Fibonacci sequence
        x_n = x_n_1_plus + x_n
        # Calculate next number that is prime
        x_n_1_plus = 4 * x_n_1 + x_n_2
        x_n_2 = x_n_1
        x_n_1 = x_n
    return x_n

