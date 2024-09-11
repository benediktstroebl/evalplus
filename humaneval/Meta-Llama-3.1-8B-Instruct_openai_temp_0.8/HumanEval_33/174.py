```python
def sort_third(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, 
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.

    :param l: Input list
    :return: Sorted list at indices divisible by 3
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(l) if j % 3 == 0])[k] for k, i, x in enumerate(l)]

# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

In this script, the function `sort_third` uses a list comprehension to create a new list. The new list's value at index `i` is equal to the old list's value at index `i` if `i` is not divisible by 3. If `i` is divisible by 3, the new list's value at index `i` is the `k-th` value in the sorted list of values from the old list at indices that are divisible by 3. The `enumerate` function is used to get both the index and value of each element in the old list, and the `sorted` function is used to sort the list of values at indices that are divisible by 3. The `if j % 3 == 0` condition filters the list to only include values at indices that are divisible by 3.