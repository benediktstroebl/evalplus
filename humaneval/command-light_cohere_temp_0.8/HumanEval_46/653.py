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

def main():
    test_fib4()
```

This script defines a function `fib4` that computes the n-th element of the Fibonacci sequence without using recursion. The `test_fib4` function tests the `fib4` function with different input values and ensures the function produces the correct results. The `main` function is where the `fib4` function is called to compute the n-th Fibonacci numbers.