```markdown
### Maximum Element in a List

#### Solution

```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    
    # Check if the list is empty
    if not lst:
        raise ValueError("List cannot be empty")
    
    # Use the built-in max function with the list as an argument
    # This will return the maximum element in the list
    return max(lst)
```

#### Example Usage

```python
# Test the max_element function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

#### Time Complexity

The time complexity of this solution is O(n), where n is the number of elements in the list. This is because the built-in max function scans the entire list to find the maximum element.