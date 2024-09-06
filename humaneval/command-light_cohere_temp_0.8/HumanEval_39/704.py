```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is also prime.
    Returns None if n < 1
    """
    if n < 1:
        return None
    
    fib = [0, 1]
    for _ in range(2, n + 1):
        if fib[-1] > sqrt(3):
            fib.append(fib[-1] + fib[-2])
        else:
            fib.append(fib[-1])
    
    for num in fib:
        if num <= sqrt(3):
            return num
```