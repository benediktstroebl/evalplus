```python
def sort_third(lst):
    """This function sorts the list l such that values at indices divisible by three are in their correct relative order.
    
    Args:
        lst (list) --> input list
    """
    # Initialize a new list l' with all elements of l
    lst_copy = [x for x in lst]
    # Sort lst_copy such that elements divisible by three come first
    lst_copy.sort_by_key(lambda x: x // 3, lst_copy)
    # Return lst_copy
    return lst_copy

# Test cases
print(sort_third([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
```