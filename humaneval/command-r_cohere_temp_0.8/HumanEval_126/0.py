```python
def is_sorted(lst):
    '''
    Checks if list of integers is sorted in ascending order and has no duplicates.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if list is sorted and has no duplicates. False otherwise.
    '''
    # Check for duplicates
    if len(lst) != len(set(lst)):
        return False

    # Check if sorted
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False

    return True
```