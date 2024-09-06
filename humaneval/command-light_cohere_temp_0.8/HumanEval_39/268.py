Here's a solution:
```python
def prime_fib(n):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            a, b = min(a, b + 2), b + 1
        return a
```
This function, `prime_fib`, calculates the n-th Fibonacci number that is prime and returns it. 

It starts with the basic assumption of the first two numbers being 2 and 3, then iteratively calculates the next numbers in the sequence until the desired result is reached.

This function is self-contained and does not require any additional imports or functions.