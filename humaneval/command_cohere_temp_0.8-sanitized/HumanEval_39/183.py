def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Starts with Fibonacci number 5 (index 3)
        idx = 3
        prev_fib = 0
        curr_fib = 1
        num = 5
        while True:
            # Checks whether the current Fibonacci number is prime
            if is_prime(num):
                if n == 1:
                    return num
                n -= 1
            # Update the Fibonacci number and the index where it starts
            idx += 1
            if idx > 50:
                break
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
            num = prev_fib + curr_fib

        # If we reach this line, it means we didn't find a prime Fibonacci number in time
        # So we revert to a slower method and check each number individually
        for i in range(3, n + 2):
            if is_prime(i) and i % 2 == 0:
                return i

        return None