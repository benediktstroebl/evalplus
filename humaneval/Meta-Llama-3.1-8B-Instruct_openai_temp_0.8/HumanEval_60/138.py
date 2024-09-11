### Python Script: sum_to_n Function

Here's a self-contained Python script with the `sum_to_n` function as per your requirements:

```markdown
## sum_to_n Function

This function calculates the sum of numbers from 1 to n.

### Code

```python
def sum_to_n(n: int) -> int:
    """
    sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return n * (n + 1) // 2
```

### Explanation

The `sum_to_n` function uses the formula `n * (n + 1) / 2` to calculate the sum of numbers from 1 to n. This formula is derived from the formula for the sum of an arithmetic series.

### Usage

You can use the `sum_to_n` function like this:

```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

### Time Complexity

The time complexity of the `sum_to_n` function is O(1), making it very efficient for large inputs.
```