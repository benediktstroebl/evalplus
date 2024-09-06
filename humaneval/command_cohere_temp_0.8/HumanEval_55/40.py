```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number, using recursion with a base case to handle n=1 and n=2, which are the first two numbers in the series. For larger `n`, it recursively calls itself with `n-1` and `n-2`, adds the results, and returns the sum. This means the height of the recursion tree grows logarithmically, reducing the time complexity compared to a direct recursive approach.