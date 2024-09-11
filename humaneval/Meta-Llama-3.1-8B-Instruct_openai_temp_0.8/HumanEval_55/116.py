### Fibonacci Number Generator
Here's a Python script that provides an implementation of the Fibonacci sequence using both iterative and recursive methods.

#### Code
```markdown
def fib_iterative(n: int) -> int:
    """Return n-th Fibonacci number using iterative method.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The Fibonacci number at position n.
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def fib_recursive(n: int) -> int:
    """Return n-th Fibonacci number using recursive method.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The Fibonacci number at position n.

    Raises:
    RecursionError: If n is greater than the maximum recursion depth.
    """
    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def main():
    n = 10  # Change this to test the function with a different value of n
    print(f"The {n}-th Fibonacci number using iterative method is: {fib_iterative(n)}")
    print(f"The {n}-th Fibonacci number using recursive method is: {fib_recursive(n)}")


if __name__ == "__main__":
    main()
```

#### Usage
To run the script, save it to a Python file (e.g., `fibonacci.py`) and execute it using your Python interpreter (e.g., `python fibonacci.py`). You can adjust the value of `n` in the `main` function to test the script with different Fibonacci numbers.

Note: The recursive implementation has a high time complexity due to repeated calculations, which can lead to a RecursionError if n is large. The iterative implementation is generally more efficient and recommended for large values of n.