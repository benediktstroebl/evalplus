```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It checks if `n` is less than or equal to 1, returning `n` directly if so. If `n` is greater than 1, it returns the sum of the two preceding Fibonacci numbers by recursively calling itself with arguments `n-1` and `n-2`, which represents the (n-1)-th and (n-2)-th Fibonacci numbers, respectively. 

This recursive approach avoids repeated calculations, making it more efficient than computing each Fibonacci number individually.