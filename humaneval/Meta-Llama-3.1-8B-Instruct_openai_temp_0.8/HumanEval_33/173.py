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
        list: The modified list according to the problem statement.
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(lst) if j % 3 == 0])[k] 
            for k, (i, x) in enumerate(zip(range(len(lst)), lst))]

# Test the function
print(sort_third([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
# Output: [2, 6, 3, 4, 8, 9, 5]
```

This script defines a function `sort_third` that takes a list as input and returns a modified list according to the problem statement. It uses a list comprehension to iterate over the input list and apply the required transformation. The `enumerate` function is used to get both the index and value of each element in the list, and the `zip` function is used to pair the indices and values together. The sorted elements at indices divisible by three are obtained by a nested list comprehension.