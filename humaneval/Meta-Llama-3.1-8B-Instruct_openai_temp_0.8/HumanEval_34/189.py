### Python Script to Remove Duplicates from a List and Return Unique Elements in Sorted Order

Here is a Python function that uses a set to remove duplicates and then returns the elements in sorted order:

```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
        l (list): Input list

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    sorted_unique_list = sorted(list(unique_set))
    
    return sorted_unique_list

# Example usage:
if __name__ == "__main__":
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(input_list))  # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input and returns a new list containing the unique elements in sorted order. It uses a set to remove duplicates because sets in Python cannot contain duplicate values. The set is then converted back to a list and sorted in ascending order before being returned. The script also includes an example usage of the function.