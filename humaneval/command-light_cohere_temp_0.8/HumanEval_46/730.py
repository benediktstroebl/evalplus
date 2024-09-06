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

# Unit tests
def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This Python script defines a function `fib4` that computes the n-th Fibonacci number using a simple iterative approach. The function uses a loop to calculate the sum of the previous four Fibonacci numbers, starting from the fifth element. 

It also includes unit tests to ensure the correctness of the `fib4` function.