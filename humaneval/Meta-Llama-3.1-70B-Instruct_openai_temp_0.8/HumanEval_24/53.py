```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Raises:
    ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

def main():
    print(largest_divisor(15))  # Output: 5

if __name__ == "__main__":
    main()
```

This script defines a function `largest_divisor` that takes an integer `n` and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n - 1` to `1` and returns the first number that divides `n` without leaving a remainder. If `n` is less than 1, it raises a `ValueError`.

The `main` function is used to test the `largest_divisor` function with the example input `15`, and the result is printed to the console.