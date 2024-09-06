```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next((c for c in (a, b) if c <= n)), a + b
    return a
``` 
This function calculates the n-th Fibonacci number that is prime and returns it. It uses a strategy of iterating up to n, checking each candidate as a Fibonacci number to see if it's less than n, and then incrementing by adding the last two together.