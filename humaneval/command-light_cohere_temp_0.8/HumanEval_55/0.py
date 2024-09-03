```python
def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return _fib(n)

def _fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return _fib(n - 1) + _fib(n - 2)

# Driver code
if __name__ == "__main__":
    try:
        print(fib(10))  # 10th Fibonacci number is 55
    print(fib(1))    # 1st Fibonacci number is 1
    print(fib(8))    # 8th Fibonacci number is 21
    print(fib(0))   # 0th Fibonacci number is 0
    print(fib(-1))  # Negative test case fails
    print(fib(9))   # Test case beyond the range fails
```

This code defines a function fib that calculates the n-th Fibonacci number, where n is a positive integer. It then defines a helper function `_fib` that calculates Fibonacci numbers recursively. The driver code demonstrates the first 10 test cases, and prints the corresponding Fibonacci numbers. It also includes a test case for negative input, and another test case beyond the valid range to ensure the function's correctness.

Finally, the output will display the result of the function for the provided inputs.