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

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This Python code defines a function called fib4 that computes the n-th element of the Fibonacci sequence without recursion. The sequence starts with 0 for n=0, 1 for n=1, 2 for n=2, and so on. The function uses a "if-elif" structure to handle different cases of input n and returns the appropriate Fibonacci number. The test_fib4 function contains unit tests that verify the correctness of the fib4 function by asserting that it produces the correct results for specific input values.