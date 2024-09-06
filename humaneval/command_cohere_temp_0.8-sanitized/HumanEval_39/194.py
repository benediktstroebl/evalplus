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
def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Find nth prime Fibonacci number
        limit = 10 ** 5
        fib_primes = [2, 3]
        prev_fib, curr_fib = 2, 3
        count = 0
        for num in range(4, limit + 1):
            if is_prime(num):
                fib_primes.append(num)
                if num == prev_fib + curr_fib:
                    count += 1
                    prev_fib, curr_fib = curr_fib, num
                elif num == prev_fib - curr_fib:
                    prev_fib = num
                else:
                    curr_fib = num
                    
        # Verify if the count is the desired 'n' or exceed it
        return fib_primes[n - 1] if count >= n else None