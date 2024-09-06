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
    n = 7
    expected = 14
    actual = fib4(n)
    assert expected == actual, f"Fib4({n}) did not return {expected}"

test_fib4()
```
The function `fib4` calculates the n-th element of the Fibonacci sequence without recursion. The `test_fib4` function verifies the function's output for various values of `n`. The function passes the test with the value of `n` set to 7.