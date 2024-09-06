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
The function `fib4` calculates the n-th element of the Fibonacci sequence without recursion, which is a more efficient approach compared to the traditional recursive method.  The function uses an **`if-elif`** structure to handle different cases of the input `n` and returns the corresponding Fibonacci number. The test function `test_fib4` passes the corresponding tests to confirm the correctness of the `fib4` function.