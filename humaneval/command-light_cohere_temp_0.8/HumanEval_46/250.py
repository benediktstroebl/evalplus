```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage
fib = fib4(7)
print("Fibonacci of 7 is:", fib)
```
The code defines a Python function `fib4` that computes the nth Fibonacci number in the Fibonacci sequence using a formula. The function first checks if `n` is 0, 1, or 2 and returns the corresponding number. If `n` is not 0, 1, or 2, it recursively calls itself with the argument `n-1`, `n-2`, `n-3`, or `n-4` to compute the Fibonacci number for `n`. The function then returns the computed Fibonacci number.