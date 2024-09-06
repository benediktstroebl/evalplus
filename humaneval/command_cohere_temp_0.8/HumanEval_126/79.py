```python
def is_sorted(lst):
    return all(e < lst[i+1] for i, e in enumerate(lst) if i + 1 < len(lst)) and len(set(lst)) == len(lst)
```

The function leverages two conditions to solve the problem:
1. **Sort order condition**: This condition checks whether the list elements are sorted in ascending order by utilizing a generator expression, which iterates through adjacent elements and returns True if they are in order and False if there is a deviation from sorted order.
2. **Duplicate check condition**: This condition checks whether there are duplicate elements in the list by using the `set()` function to convert the list to a set, which removes duplicate elements and converts it back to a list. If the lengths of the original and converted lists are the same, then no duplicates exist.

The `all()` function is then used to evaluate whether both conditions are met, returning True if the list is sorted with no duplicates and False otherwise.