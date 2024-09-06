```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It bases the computation on the nature of the series, that each number is the sum of the two preceding ones. This allows the function to traverse the series with good efficiency, making it a useful tool for various applications that require Fibonacci numbers.