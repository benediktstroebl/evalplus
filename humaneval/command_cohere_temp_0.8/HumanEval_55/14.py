```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function leverages recursion to compute the Fibonacci number for a given input `n`. It employs two base cases: when `n` is 1 or 0, it returns `n` directly, considering these numbers to be the first two digits of the sequence. For `n` greater than 2, it invokes itself recursively on `n-1` and `n-2`, adding the results to compute the Fibonacci number.