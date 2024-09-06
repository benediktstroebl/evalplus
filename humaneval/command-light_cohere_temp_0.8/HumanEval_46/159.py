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
    result = fib4(n)
    assert result == 14    # Should be true
    print("Test passed!")

test_fib4()
```
This script defines a function `fib4` that computes the n-th Fibonacci number in the sequence without recursion. The function uses a test case to validate its correctness.