```markdown
### Unique Elements in a List
#### Problem Statement
Return a sorted list of unique elements from the input list.

#### Solution
```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list

    Args:
        lst (list): The input list

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

#### Explanation
This script defines a function `unique` that takes a list as input and returns a sorted list of unique elements. It uses the built-in `set` function to remove duplicates and the `sorted` function to sort the resulting list. The example usage demonstrates how to call the function with a sample list.
```