```python
def sort_third(lst: list):
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the indices that are not divisible by three,
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of lst, but sorted.
    
    Args:
        lst (list): The input list.
    
    Returns:
        list: The output list with values at indices divisible by three sorted.
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(lst) if j % 3 == 0])[k] 
            for k, x in enumerate(lst) if k % 3 == 0]
```

Here's an explanation of the code:

1. We use a list comprehension to create a new list, `lst'`.
2. For each element `x` in `lst`, we check if its index `i` is not divisible by 3. If it's not, we simply include `x` in `lst'`.
3. If `i` is divisible by 3, we find the values of elements at indices divisible by 3 in `lst`, sort them, and include the `k-th` element of the sorted list in `lst'`. Here, `k` is the index of `x` in `lst`.
4. We use the `enumerate` function to get both the index and value of each element in `lst`, and the `if k % 3 == 0` condition to only include elements at indices divisible by 3 in the sorted list.

### Example Usage
```python
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```