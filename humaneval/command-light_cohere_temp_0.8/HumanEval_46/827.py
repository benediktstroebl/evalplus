```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which the next number is defined as the sum of the two preceding ones.
    if n <= 1:
        return 0
    elif n <= 2:
        return 2
    elif n <= 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fibonacci(n):
    assert fib4(n) == fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4), "Error: Function did not return the correct result."

# Example usage
test_fibonacci(5)
```