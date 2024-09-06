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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

# Unit tests
def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This code defines a Fibonacci sequence function using the recursive approach. The function calculates the result for the nth element in the Fibonacci sequence using recursion and returns the result. The function is also tested using the test_fib4 function with the corresponding assertions.