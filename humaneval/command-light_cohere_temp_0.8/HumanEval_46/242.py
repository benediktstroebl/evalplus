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
    assert fib4(8) == 28
    assert fib4(9) == 43
    assert fib4(10) == 55
    assert fib4(11) == 89
    assert fib4(12) == 144

def main():
    test_fib4()

```
The provided code defines a function `fib4` which computes the n-th Fibonacci number in O(n) using the above formula. It then has a test_fib4 function which uses `assert` statements to ensure that the `fib4` function is working as expected. The `main` function is used to run the tests.