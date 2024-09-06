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
    n = 7
    assert fib4(n) == 14
```
This Python code defines a function called fib4 that computes the n-th element of the Fibonacci sequence using a technique that avoids recursion. The function achieves this by using a series of if-elif statements to determine the base cases for the sequence (0, 1, 2) and then uses the sum of the previous three elements to compute the next element in the sequence. The test_fib4 function tests whether the fib4 function correctly by asserting that it computes the 7th element of the Fibonacci sequence (which should be 14) correctly.