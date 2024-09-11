```python
def sort_third(lst: list) -> list:
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the indices that are not divisible by three, 
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of lst, but sorted.

    Args:
        lst (list): The input list.

    Returns:
        list: The modified list.
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(lst) if j % 3 == 0])[i % 3] for i, x in enumerate(lst)]


# Test the function
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script defines the `sort_third` function, which takes a list `lst` as input and returns a modified list. The function uses a list comprehension to iterate over the input list. If the index `i` is not divisible by 3, the value at this index is taken as is. If the index is divisible by 3, the value at this index is taken from the sorted list of values at indices that are divisible by 3. The function then prints the results of calling `sort_third` with the example lists.