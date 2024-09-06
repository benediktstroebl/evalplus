```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the Fibonacci number for n by recursively calling itself with arguments `n-1` and `n-2`, relying on the fact that the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers for n greater than 1. For n equal to 1, it directly returns n. This approach efficiently computes Fibonacci numbers without storing the entire sequence.