### Unique Elements in a List

Here's a Python script that defines a function `unique` to return a sorted list of unique elements:

```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list

    Returns:
        list: Sorted list of unique elements

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert list to a set to remove duplicates and then convert back to list
    unique_list = list(set(l))
    
    # Sort the list in ascending order
    unique_list.sort()
    
    return unique_list

# Example usage:
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(input_list))
```

When you run this script, it will output the sorted list of unique elements from the input list: `[0, 2, 3, 5, 9, 123]`.