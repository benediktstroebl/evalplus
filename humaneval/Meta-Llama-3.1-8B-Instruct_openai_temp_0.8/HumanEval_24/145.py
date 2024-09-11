### Largest Divisor
#### Problem Statement
Find the largest number that divides a given number `n` evenly, smaller than `n`.

#### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

#### Explanation
This function works by iterating from `n - 1` down to `1` (exclusive) and checking each number to see if it divides `n` evenly. The first number that does is the largest divisor smaller than `n`, so we return it immediately.

#### Example Use Cases
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 7
```