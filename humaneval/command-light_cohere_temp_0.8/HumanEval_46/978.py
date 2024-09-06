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
This Python code defines a function called fib4 that computes the n-th element of the Fibonacci sequence using a loop-based approach. The function initially checks for base cases: if n is 0, it returns 0. If n is 1, it returns 0. If n is 2, it returns 2. If n is 3, it returns 0. Otherwise, the function recursively calls itself with the argument (n-1), adding the results of previous three recursive calls to compute the n-th Fibonacci number. 

This code tests the fib4 function with various input values, ensuring the function correctly computes the Fibonacci numbers and passes all the tests.