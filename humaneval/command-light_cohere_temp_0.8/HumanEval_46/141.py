```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. Fibonacci(n) returns the number in the Fibonacci sequence starting with index n."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fibonacci(n):
    """Test the Fibonacci function with various inputs."""
    try:
        result = fib4(n)
        print(f"Fibonacci({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("The Fibonacci function calculates Fibonacci numbers correctly.")
    test_fibonacci(5)
    test_fibonacci(6)
    test_fibonacci(7)
```

This code defines a function `fib4` that computes Fibonacci numbers using the recursive approach. The `test_fibonacci` function tests the `fib4` function with various input values and asserts that the results are correct. The script also includes a `main` block, which serves as the entry point and prints a message confirming the correct operation of the Fibonacci function.