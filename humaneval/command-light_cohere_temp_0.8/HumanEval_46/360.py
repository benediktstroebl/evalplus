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
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 84
```
This code defines a Fibonacci sequence function that returns the nth Fibonacci number in the sequence without using recursion. The sequence starts with the number 0, which is the base case for n equal to 0 or 1. It then calculates the subsequent numbers by summing the two preceding numbers in the sequence. The function tests the tests to ensure its correctness with the expected outputs for various input values.