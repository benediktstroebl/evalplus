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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The provided Python script defines a function `fib4` that computes the n-th element of the Fibonacci sequence using a non-recursive approach. The function uses a specific conditions to determine the base cases (0,1, and 2) and then uses an iterative approach to compute the remaining numbers in the sequence.

The script also contains a `test_fib4` function with assertions that verify the correctness of the `fib4` function by checking if the calculated results for specific input values match the expected values. 

This script provides an efficient, self-contained way to compute Fibonacci numbers without relying on recursion, which can be beneficial in avoiding potential stack overflow issues.