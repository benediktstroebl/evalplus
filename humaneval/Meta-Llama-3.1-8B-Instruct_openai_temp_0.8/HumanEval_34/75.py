### Unique Elements in a List
#### Description
This script solves the problem by defining a function `unique` that takes a list as input and returns a sorted list of unique elements.

#### Code
```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))  # Convert list to set (removing duplicates) and sort

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

#### Explanation
The solution uses the built-in `set` data structure in Python to remove duplicate elements from the input list. Since sets in Python cannot contain duplicate elements, this automatically removes all duplicates. The `sorted` function is then used to sort the unique elements in ascending order before returning them.