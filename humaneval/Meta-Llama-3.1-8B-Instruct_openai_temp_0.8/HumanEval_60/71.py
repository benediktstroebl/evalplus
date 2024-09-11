### Summation Function in Python
#### Code

```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the summation.

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
    return sum(range(1, n + 1))

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

#### Explanation
This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the built-in `sum` function and the `range` function. The `range` function generates a sequence of numbers from 1 to `n` (exclusive), and the `sum` function adds up these numbers. The result is returned by the function. The example usage demonstrates how to call the function with different values of `n`.