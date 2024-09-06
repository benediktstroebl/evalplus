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
This code defines a function `fib4` that computes the nth element of the Fibonacci sequence using the recursive approach. The `test_fib4` function tests the `fib4` function with different input values and asserts that the results are correct. 

The code is self-contained and does not rely on any external functions or modules. It is a way of implementing the Fibonacci sequence calculation in a standalone and efficient manner.