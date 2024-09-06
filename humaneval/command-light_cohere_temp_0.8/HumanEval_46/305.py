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
    n = 5
    expected = 4
    actual = fib4(n)
    assert actual == expected, f"Incorrect result: {actual} != {expected}"

# Call the function to test it
test_fib4()
```

This code defines a function called fib4 that computes the n-th element of the Fibonacci sequence using a loop-free approach. It uses an if-elif structure to handle different cases of the input n, and the function returns the calculated value. The test_fib4 function then tests the fib4 function by passing a value of n = 5 and comparing the calculated result with the expected value (4 in this case). If the actual result matches the expected value, the test passes; otherwise, it fails, and an error message is displayed.