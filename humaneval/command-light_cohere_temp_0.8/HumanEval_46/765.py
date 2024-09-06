```python
def fib4(n: int):
    if n <= 0:
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
The Fibonacci sequence, a mathematical sequence where each number is the sum of the two preceding ones, is defined using this function. The function checks the input n, and if it's less than 0, returns 0. If it's equal to 1, it returns 0. If it's equal to 2, it returns 2. If it's equal to 3, it returns 0. Otherwise, it calls itself recursively, adding up the preceding four numbers to compute the next one.

The test_fib4 function ensures that the function works correctly by passing the tests with the specified input values.