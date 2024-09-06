```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent term is the sum of the previous two terms.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        a = 0
        b = 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Unit tests
def test_fib4():
    assert fib4(5) == 4  # Should return 4
    assert fib4(6) == 8  # Should return 8
    assert fib4(7) == 14  # Should return 14

if __name__ == "__main__":
    test_fib4()
```
The function computes the n-th element of the Fibonacci sequence using an iterative approach without recursion. The function returns the main body.