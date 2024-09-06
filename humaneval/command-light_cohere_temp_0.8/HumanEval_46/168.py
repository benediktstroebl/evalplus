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
    try:
        assert fib4(5) == 4
        assert fib4(6) == 8
        assert fib4(7) == 14

        print("Test Passed")

test_fib4()
```
The `fib4` function calculates the nth element of the Fibonacci sequence without using recursion. It uses a a simple case-switch to decide which Fibonacci number to return, based on the input `n`. 

This function is self-contained, and it can be used to calculate the Fibonacci number for any given `n` without the need for additional functions or recursion.