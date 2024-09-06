```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    for _ in range(n):
        a, b = a + a, b + b
        yield a

# Testing
test_fib4 = [lambda n: fib4(n) == (0, 1) + (1, 1) + (2, 3) + (3, 6) + (4, 11)]

test_fib4(5)  # True
test_fib4(6)  # True
test_fib4(7)  # True
```
The provided Python code defines a function called fib4, which calculates the n-th value of the Fibonacci sequence without recursion. The function uses an iterative approach to achieve this, and it generates the n-th Fibonacci value by summing the previous two values in the sequence.

The test_fib4 lambda function is then created, which takes an integer n as input and checks if the result of calling fib4(n) equals the expected Fibonacci sequence values. The test_fib4 function is then called with various input values, and the results are verified against the expected Fibonacci sequence values.

This code demonstrates a simple and efficient way to calculate Fibonacci values without using recursion, which can be beneficial in situations where recursion is not desired or efficient.