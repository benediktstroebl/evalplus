```markdown
# Solution to the below_threshold problem
=====================================

This Python script provides a function `below_threshold` that checks if all numbers in a given list are below a specified threshold.

```python
def below_threshold(lst: list, t: int) -> bool:
    """
    Return True if all numbers in the list are below threshold t.

    Args:
    lst (list): The list of numbers to check.
    t (int): The threshold to compare with.

    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < t for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False
```

In this solution, we use the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements of the iterable are true, and `False` otherwise. This approach is concise and efficient, making it a good fit for this problem.