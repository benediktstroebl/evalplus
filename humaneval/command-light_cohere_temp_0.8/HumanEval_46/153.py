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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 84
    assert fib4(11) == 145

# Run the function and test cases
test_fib4()
```
This code defines a function called fib4 which calculates the n-th element of the Fibonacci sequence using the recursive definition. The test_fib4 function tests the function by calling it with various input values and asserting that the results are correct.