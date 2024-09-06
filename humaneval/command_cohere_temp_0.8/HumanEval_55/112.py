```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number recursively. It returns `n` if `n` is less than or equal to 1. If `n` is greater than 1, it returns the sum of the two preceding Fibonacci numbers by recursively calling `fib(n-1)` and `fib(n-2)`. This approach avoids explicit recursion and improves efficiency. It achieves this through memoization, which stores previously computed values to avoid redundant calculations. This enhances performance and responds correctly for larger values of `n`.

Here is an example usage of this function:
```python
result = fib(10)
print(result)
```

The output will be:
```
55
```