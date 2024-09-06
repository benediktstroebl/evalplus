```python
def fib4(n: int):
    """The Fibonacci sequence without recursion."""
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. This sequence begins with 0 and 1, and each subsequent number is the sum of the two preceding ones. The function `fib4` computes the n-th element of the Fibonacci sequence without recursion. The function uses two variables, `a` and `b`, to keep track of the last two Fibonacci numbers. The variable `for` is used to iterate through the sequence, and the values of `a` and `b` are updated in each iteration using the assignment statement.

The `test_fib4` function tests the `fib4` function with various input values and asserts that the function returns the correct result. The output will be displayed if the test passes without errors.