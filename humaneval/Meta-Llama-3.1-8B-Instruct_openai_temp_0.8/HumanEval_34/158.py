### Unique Elements in a List
#### Problem Description
This script solves the problem of returning a sorted list of unique elements from a given list.

#### Code
```python
def unique(input_list: list) -> list:
    """Return sorted unique elements in a list
    Args:
        input_list (list): The list of elements

    Returns:
        list: A sorted list of unique elements
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    return sorted_list

# Example usage
if __name__ == "__main__":
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(input_list))
```

#### Explanation
This script uses Python's built-in `set` data type to remove duplicate elements from the input list. Then, it converts the set back to a list and sorts it using the `sorted` function. The resulting sorted list of unique elements is then returned.

Note that the order of elements in a set is not guaranteed, so if you need to preserve the original order of elements, you may need to use a different approach.