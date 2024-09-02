

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
    if n == 1:
        return 2
    if n == 2:
        return 3

    # Find prime numbers between 2 and Fn
    # --------------------------------------------------------------------------
    prime_numbers = [2]
    curr_num = 3

    # find prime numbers up to 10**9
    while curr_num <= 10**9:

        # check if curr_num is prime
        is_prime = True
        for prime in prime_numbers:
            if curr_num % prime == 0:
                is_prime = False
                break

        # curr_num is prime, add to prime_numbers
        if is_prime:
            prime_numbers.append(curr_num)

        # go to next number
        curr_num += 2

    # find Fn
    # --------------------------------------------------------------------------
    fib_nums = [1, 1]
    curr_fib = 2

    # find Fibonacci numbers until Fn
    while curr_fib < 10**9:
        last_fib = fib_nums[-1]
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        curr_fib = fib_nums[-1]

    # find Fibonacci number that is also prime
    # --------------------------------------------------------------------------
    for i in range(len(fib_nums)):
        for prime in prime_numbers:
            if prime == fib_nums[i]:
                return fib_nums[i]
    return -1
