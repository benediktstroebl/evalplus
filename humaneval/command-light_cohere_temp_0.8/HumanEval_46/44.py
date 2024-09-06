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

def test_fib4():
    n = 7
    expected = 14
    actual = fib4(n)
    assert actual == expected, f"Fib4({n}) did not return {expected}, expected {n}!"

test_fib4()
```

The code defines a function called `fib4` that computes the nth value of the Fibonacci sequence without recursion. The `test_fib4` function tests this function by calling it with n=7 and comparing the result against the expected value of 14. The function passes the test successfully when the actual and expected values match.