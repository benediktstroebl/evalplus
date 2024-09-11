```python
def sort_third(lst):
    """This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the indices that are not divisible by three, 
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of lst, but sorted.
    
    Args:
        lst (list): The input list.
    
    Returns:
        list: The sorted list.
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(lst) if j % 3 == 0])[k] 
            for k, i, x in enumerate(range(len(lst)))]
```

Example usage:

```python
print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]
```