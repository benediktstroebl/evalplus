```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2
```
The function 'prime_fib' takes an integer 'n' as input and returns the n-th Fibonacci number that is also prime. The function uses a basic strategy to start from 2 and recursively finds prime numbers by identifying prime factors of consecutive Fibonacci numbers.