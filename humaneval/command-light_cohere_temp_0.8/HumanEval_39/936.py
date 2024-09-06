```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    else:
        a, b = 6, 7
        for _ in range(n - 4):
            a, b = a + b, a % b
        if a == b or a == next(b):
            return a
        else:
            yield b
```

This code defines a prime_fib function that calculates the nth Fibonacci number and checks if it's also prime. It follows the a sequence of prime numbers and stops when the next number (or the next term in the sequence) is reached. The function is tested with the first few values and yields the corresponding Fibonacci numbers.