

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
    # Build prime list up to the input
    prime_list = [2]
    num = 3
    while len(prime_list) <= n:
        if num % 2 == 0 or num % 3 == 0:
            pass
        else:
            prime_list.append(num)
        num += 2

    # Build Fibonacci sequence up to the input
    fib_seq = [0, 1]
    num_a = 0
    num_b = 1
    while len(fib_seq) <= n:
        next_num = num_a + num_b
        fib_seq.append(next_num)
        num_b = num_a + num_b
        num_a = num_b

    # Make a list of prime Fibonacci numbers
    prime_fib_nums = []
    for i in range(len(prime_list)):
        for j in range(len(fib_seq)):
            if prime_list[i] == fib_seq[j]:
                prime_fib_nums.append(prime_list[i])

    return prime_fib_nums[n-1]

