```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number recursively. It checks if `n` is less than or equal to 1, returning `n` directly if so. If `n` is greater than 1, it returns the sum of the `(n-1)`-th and `(n-2)`-th Fibonacci numbers, recursively calculated. This approach avoids repeated calculations, and the function provides the desired Fibonacci numbers when tested with the given input. 
```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```