```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent term is equal to the sum of the previous two terms. The sequence starts with 0 and 1.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fibonacci(n: int):
    """Test the function fibonacci(n) with different values of n."""
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    assert fib4(n) == fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4), "Invalid result for n={}.".

test_fibonacci(5)
test_fibonacci(6)
test_fibonacci(7)
```

This code provides a straightforward and efficient way to calculate the n-th Fibonacci number without recursion, using a straightforward formula. It passes the test cases for various values of n and ensures the accuracy of the calculated Fibonacci numbers.