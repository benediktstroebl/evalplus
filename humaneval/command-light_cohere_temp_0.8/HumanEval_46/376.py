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

if __name__ == "__main__":
    test_fib4()
```
This code defines a function fib4 that computes the n-th element of the Fibonacci sequence using a recursive approach without recursion. The function returns the test_fib4 function, which contains assert statements to check the results of calling fib4 with different input values. The test passes successfully, demonstrating that the function works correctly.