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
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 84

if __name__ == "__main__":
    test_fib4()
```
The code above defines a function called `fib4` that computes the nth Fibonacci number in the Fibonacci sequence using the formula `F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)`. 

The `test_fib4` function contains unit tests that use the `fib4` function. The tests ensure that function correctly computes Fibonacci numbers up to a certain index. 

This code is self-contained and does not require external dependencies to function. The tests can be run directly within the Python interpreter or with a testing framework.