```python
def fib4(n: int):
    if n == 0 or n == 1:
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
The provided code defines a Fibonacci number sequence using the Fibonacci sequence formula. The n-th element in the sequence is calculated by summing the preceding four elements. The code successfully passes the test cases, which is the definition of the Fibonacci sequence and the value of the n-th element for n = 5, 6, and 7. This demonstrates the expected behavior of the Fibonacci sequence.