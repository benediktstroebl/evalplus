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
```
This code defines a function called `fib4()` that computes the n-th element of the Fibonacci sequence using the recursive definition. The function checks for base cases (n=0,1,2,3) and returns the appropriate values. If n is greater than these base cases, the function recursively calls itself to compute the next element in the sequence. 

The `test_fib4()` function then tests the `fib4()` function with various input values. The function asserts that the values returned by `fib4()` match the expected results, passing the tests.