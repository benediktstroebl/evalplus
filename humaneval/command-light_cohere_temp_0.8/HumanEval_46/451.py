```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is equal to the sum of the two preceding ones. The Fibonacci sequence can by summing the last two numbers in the sequence to generate the next one. The function returns the value of the n-th Fibonacci number in the sequence."""
    return (n < 2) ^ (n & 1) + fib4(n-1) + fib4(n-2) + fib4(n-3)

# Test the function
def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The function takes an integer n as input and returns the n-th Fibonacci number in the sequence.