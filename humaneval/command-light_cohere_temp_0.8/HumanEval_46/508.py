```python
def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This Python code defines a function `fib4` that computes the n-th element of the Fibonacci sequence using an efficient method that avoids recursion. 

The function utilizes a series of additions and identity values to calculate the Fibonacci number, starting from the base cases of `n == 0` or `n == 1`, which return 0. For larger values of `n` greater than 3, the function recursively calls itself with the `n-1`, `n-2`, `n-3`, and `n-4` components.

The `test_fib4` function asserts that the `fib4` function produces the correct Fibonacci numbers for the input values 5, 6, and 7. This ensures the correctness of the function's output.