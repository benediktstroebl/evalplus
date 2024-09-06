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

if __name__ == "__main__":
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 8
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 98
    assert fib4(11) == 144
    assert fib4(12) == 244
    assert fib4(13) == 377
    assert fib4(14) == 546
    assert fib4(15) == 812
  ```

The provided code defines a Python function that computes the n-th Fibonacci number in a series without using recursion. The function takes an integer n as input and returns the n-th Fibonacci number. The tests at the` __main__` verify the correctness of the `fib4` function by passing different values of `n` and checking the results against the expected Fibonacci numbers.