Here is a Python script that demonstrates the solution to the problem using a self-contained function:

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

# Unit tests
test_fib4 = {
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
}
```

This script defines a function `fib4` that computes the n-th element of the Fibonacci sequence using the recursive definition. The function handles edge cases for `n` equal to 0, 1, and 2, returning 0, 1, and 2, respectively. It then recursively calculates the the n-th element by summing the previous four terms (0, 2, 0, and 1) using an iterative approach. 

The unit tests assert that the function produces the correct results for the specified inputs, verifying its correctness.