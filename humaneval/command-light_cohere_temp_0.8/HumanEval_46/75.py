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
    assert expected == actual, f"Test failed: expected {expected}, got {actual}"

# Run the test
test_fib4()
```

This Python script defines a function `fib4` which computes the n-th Fibonacci number in the Fibonacci sequence using a loop-free approach. The function initially checks if `n` is 0, 1, or 2, returning 0, 0, or 2 respectively. If `n` is greater, the function recursively calls itself to compute the Fibonacci number. The test function `test_fib4` contains an assertion that checks if the computed Fibonacci number at position `n` matches the expected value. The script's test passes successfully when executed, confirming the correctness of the `fib4` function.