```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    
    if n < 2:
        return 0
    elif n == 1:
        return 1
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = 7
    assert fib4(n) == 14

def main():
    test_fib4()
```