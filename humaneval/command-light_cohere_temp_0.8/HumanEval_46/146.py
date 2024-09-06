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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 56
    assert fib4(11) == 89
    assert fib4(12) == 144
    assert fib4(13) == 233
    assert fib4(14) == 424
```
The function `fib4` calculates the n-th Fibonacci number in the Fibonacci sequence using a loop-based approach. The function checks for base cases where n is 0, 1, or 2, returning 0, 1, or 2 respectively. For n equal 3, it checks if n is 3 and returns 0. If n is greater than 3, it uses the recursive approach to calculate the Fibonacci number by summing up the previous four Fibonacci numbers. The function is self-contained and does not rely on any other functions or modules.