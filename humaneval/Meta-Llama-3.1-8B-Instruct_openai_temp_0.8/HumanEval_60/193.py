```markdown
### Sum of Numbers from 1 to n
#### Problem: Calculate the sum of numbers from 1 to n

Here is a Python function that solves the problem:
```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The number up to which the sum is calculated.

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


# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```
This script uses the built-in `sum` function in Python, which calculates the sum of all elements in an iterable (in this case, the range from 1 to n). The `range` function generates a sequence of numbers from 1 to n, and we add 1 to n because `range` generates numbers up to but not including n.
```