```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    while n > 0:
        a, b = a + b, a
        n -= 1
        yield a  # Return the value for the current iteration
    
# Test the function  
test_fib4 = [
    "import fib4
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
]
```
This code defines a function called `fib4` which generates the Fibonacci sequence without recursion. It starts with an initial value of [0, 1] and uses a `while` loop to generate Fibonacci numbers until the input `n` exceeds 0. The `assert` statements at the test_fib4 ensure that the function produces the correct Fibonacci numbers for the given input.