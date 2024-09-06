def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    def fibonacci_sequence(n):
        a, b = 0, 1
        for _ in range(n - 1):
            c = a + b
            a, b = b, c
        return a

    count = 0
    fib_nums = []
    a, b = 0, 1
    while len(fib_nums) < n:
        fib_nums.append(a)
        a, b = b, a + b
        count += 1
    fib_nums.append(a)
    
    prism_idx = 0
    while not is_prime(fib_nums[prism_idx]):
        prism_idx += 1

    # Return the n-th number in the Fibonacci sequence that is also prime
    return fib_nums[prism_idx]