```python
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly four positive even numbers.
    Returns:
        bool: True if n can be written as the sum of 4 even numbers, otherwise False.
    """
    # Check if n is even
    if n % 2 != 0:
        return False

    # Iterate over even numbers and check if their sum equals n
    for i in range(2, n // 2 + 1, 2):
        if (n - i) % 4 == 0:
            return True

    return False
```