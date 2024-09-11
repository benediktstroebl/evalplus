**Fibonacci Number Generator**
================================

The following Python script calculates the n-th Fibonacci number using a recursive and an iterative approach.

```python
def fib_recursive(n: int) -> int:
    """Return n-th Fibonacci number (recursive approach).

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """Return n-th Fibonacci number (iterative approach).

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n+1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


def main():
    n = 10  # Calculate the 10th Fibonacci number
    print(f"Fibonacci number at position {n}: {fib_recursive(n)} (recursive)")
    print(f"Fibonacci number at position {n}: {fib_iterative(n)} (iterative)")


if __name__ == "__main__":
    main()
```

This script defines two functions: `fib_recursive` calculates the n-th Fibonacci number using a recursive approach, while `fib_iterative` uses an iterative approach. Both functions raise a `ValueError` if `n` is a negative integer. The `main` function demonstrates how to use these functions to calculate the 10th Fibonacci number using both approaches. You can modify the value of `n` in the `main` function to calculate Fibonacci numbers at different positions.