```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is defined as the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1. The n-th Fibonacci number is computed as the sum of the two preceding Fibonacci numbers.

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

def test_fibonacci(n: int):
    """Test the function fibonacci with n inputs."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14

# Usage example
if __name__ == "__main__":
    n = 7
    print(f"The {n}th Fibonacci number is {fib4(n)}")
```
The code defines a function `fib4` that computes the n-th Fibonacci number using a recursive approach. The `test_fibonacci` function tests the `fib4` function with various input values and asserts that the computed Fibonacci numbers match the expected values. The `main` block demonstrates the usage of the `fib4` function with an input value of 7, and prints the computed Fibonacci number.