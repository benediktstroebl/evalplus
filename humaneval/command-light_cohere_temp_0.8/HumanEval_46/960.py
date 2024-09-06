```python
def fib4(n: int):
    """The Fibonacci sequence 4 numbers are defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return

def test_fib4():
    assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14

if __name__ == "__main__":
    test_fib4()
```