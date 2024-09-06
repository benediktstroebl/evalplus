```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The sequence starts with 0 and 1.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

```

This is a Python code snippet that defines a function called `fib4` that computes the nth value of the Fibonacci sequence using a loop-free approach. The function takes an integer `n` as input and returns the corresponding Fibonacci number. The function uses a specific logic to compute the Fibonacci numbers and avoids recursion by using an iterative approach.