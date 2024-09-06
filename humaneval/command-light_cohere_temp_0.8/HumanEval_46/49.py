```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers are
    general formula to generate Fibonacci numbers: 
    a = fib4(0)
    b = a + a
    c = b
    d = a
    a = c
    b = d
    c = b + a
    d = c
    return a

# Unit tests
def test_fib4():
    assert fib4(5) == 4    # Should return 4
assert fib4(6) == 8    # Should return 8
assert fib4(7) == 14    # Should return 14
```