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

# Unit tests
def test_fib4():
    assert fib4(5) == 4  # Should evaluate to 4
assert fib4(6) == 8   # Should evaluate to 8
assert fib4(7) == 14  # Should evaluate to 14

if __name__ == "__main__":
    test_fib4()
```
The code defines a Fibonacci sequence generator and passes all unit tests with the test_fib4 function. The code is self-contained, meaning it doesn't rely on external modules or functions to achieve the same result. The resulting sequence is an exponential increase in numbers, starting from 0 and increasing by the sum of the previous three numbers.