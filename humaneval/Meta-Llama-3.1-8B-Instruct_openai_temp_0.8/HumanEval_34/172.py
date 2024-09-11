### Solution: Unique Elements in a List

Here's a Python script that uses a set to remove duplicates, then sorts the result to provide the desired output:

```python
def unique_elements(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
    lst (list): The input list.

    Returns:
    list: A sorted list of unique elements.

    Example:
    >>> unique_elements([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage
if __name__ == "__main__":
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    unique_result = unique_elements(input_list)
    print("Unique elements in the list:", unique_result)
```

This script defines a function `unique_elements` that takes a list as input, converts it to a set to remove duplicates, and then sorts the resulting set to provide the unique elements in sorted order. The example usage at the end demonstrates how to use this function with a sample list.