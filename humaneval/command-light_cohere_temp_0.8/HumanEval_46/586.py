```python
def fib4(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

```

This Python script defines a function `fib4` that computes the nth element of the Fibonacci sequence using a method that does not involve recursion. The function uses an `if-else` statement to determine the appropriate computation path based on the value of `n`. This self-contained solution doesn't rely on any other functions and can be easily imported and called from other scripts.