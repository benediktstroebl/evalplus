```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.
    
    :param lst: The input list
    :return: A sorted list of unique elements
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input and returns a sorted list of unique elements. The `set` function is used to remove duplicates, and the `sorted` function is used to sort the list. 

The test at the end prints the result for the example input provided.