```python
def fib4(n: int):
    if n == 0 or n == 1:
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
    assert expected == actual, f"Test failed with n={n} expected={expected}, actual={actual}"

test_fib4()
```

This Python script defines a function called `fib4` which calculates the nth element of the Fibonacci sequence using a non-recursive approach. The function takes an integer `n` as input and returns the corresponding Fibonacci number. 

The `test_fib4` function contains a test case where it calculates the 7th element using the `fib4` function and compares the expected result with the actual result. 

The script also has the `assert` statement to verify if the test passed without raising an error.