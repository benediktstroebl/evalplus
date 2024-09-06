```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The code defines a function called fib4 that computes the n-th element of the Fibonacci sequence using the recurrence relation. The function returns the fib4(n) and returns the result, which is the n-th Fibonacci number. The test_fib4 function then asserts that the function is working correctly, and the test passes.