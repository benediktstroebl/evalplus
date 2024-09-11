Here's a Python script that implements the `sum_to_n` function:
```markdown
### sum_to_n Function

#### Description
The `sum_to_n` function calculates the sum of numbers from 1 to n.

#### Implementation
```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

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
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2
```

#### Example Usage
```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

Note that this implementation uses the formula for the sum of an arithmetic series: n * (n + 1) / 2. This formula is more efficient than iterating over all the numbers from 1 to n and summing them up.