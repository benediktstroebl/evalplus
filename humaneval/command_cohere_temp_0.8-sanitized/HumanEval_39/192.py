def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # The n-th prime Fibonacci number has the form F_n^2 - F_n-1
        prev_fib = 0
        curr_fib = 1
        count = 0
        while count < n:
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
            count += 1
        return curr_fib ** 2 - prev_fib