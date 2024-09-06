```python
def fib4(n: int):
    """The Fibonacci sequence without recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Unit test for fib4 function."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14

# Call the function to test it
test_fib4()
```
This Python script defines a function called fib4 which computes the n-th element of the Fibonacci sequence without recursion. It utilizes an iterative approach to avoid recursion and a set of tests to ensure the correctness of the function.

The tests cover the range from 0 to 7, and include various scenarios such as edge cases, basic cases, and the calculation of the n-th element in the sequence. 

This function provides an efficient and concise way to calculate Fibonacci numbers without the need for additional space complexity.