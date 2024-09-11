### below_threshold Function

The following Python script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold.

```markdown
### below_threshold Function

```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num <= threshold for num in lst)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False
```
### Explanation

This function uses the built-in Python `all()` function combined with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements in the iterable are true, and `False` if at least one element is False.

You can test this function with different input values as shown in the example usage section.