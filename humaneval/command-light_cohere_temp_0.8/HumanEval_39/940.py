Here's a self-contained Python function that calculates and returns the n-th Fibonacci number that is also prime:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            continue
        elif n % (i + 1) == 0 or n % (i + 3) == 0:
            n = n // (i + 1)
        else:
            i += 6
    return i
```
This function uses a loop to check for divisibility by checking various factors that might make the number not prime.