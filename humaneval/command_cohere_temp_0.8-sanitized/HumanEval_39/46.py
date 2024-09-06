from collections import deque
def prime_fib(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n):
        fib = deque([0, 1])
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n-1]

    if n <= 0:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return fibonacci(n//2)
    return fibonacci(n) if is_prime(fibonacci(n)) else prime_fib(n+1)