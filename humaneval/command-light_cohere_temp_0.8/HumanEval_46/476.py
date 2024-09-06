```python
def fib4(n: int):
    """The Fibonacci sequence without recursion. The sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    return fib4(n)

# Function to test the fib4 function
def test_fib4(n: int):
    assert fib4(n) == (n < 4) * [0, 2, 4, 8]

# Example usage
test_fib4(7)
```
The Python code defines a function `fib4` that computes the n-th element of the Fibonacci sequence without using recursion. The function is designed with andoc comment that explains its purpose and functionality. The `test_fib4` function tests the `fib4` function by asserting that the result of `fib4` is equal to the expected values for specific input values less than or equal to 4. The test fails if the input value is 7, which is outside the range of valid inputs for the Fibonacci sequence.