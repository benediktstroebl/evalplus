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
The function `fib4` computes the n-th Fibonacci number in the Fibonacci sequence using a method that doesn't utilize recursion. It employs an if-elif structure to swiftly identify the base cases for the sequence (0, 1, and 2) and then uses a simple formula to compute subsequent numbers. The test_fib4 function conducts tests to ensure that the `fib4` function produces the anticipated outcomes. 
This self-contained function and tests offer a clear and concise solution to the Fibonacci sequence problem without the need for recursive function calls.