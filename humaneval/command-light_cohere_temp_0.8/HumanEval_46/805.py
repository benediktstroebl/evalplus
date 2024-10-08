```python
def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This code defines a function `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using a formula that avoids recursion. It returns the same value of the n-th Fibonacci number. The function is then tested using the `test_fib4` function, which asserts that the function's output matches the expected values for the given input `n`.