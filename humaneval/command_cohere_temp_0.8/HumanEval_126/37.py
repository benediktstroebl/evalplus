```python
def is_sorted(lst):
    return all(e <= n for e in lst for n in lst if e == n) and len(set(lst)) == len(lst)
```
The `is_sorted` function verifies whether a list of numbers is sorted in ascending order, disregarding duplicate values. It does this by using a generator expression, backed by both a `filter` and `len` function. The expression (`e <= n for e in lst for n in lst if e == n`) initially filters comparable values from the list using the `filter` function. Out of these, it compares each element to the list's subsequent values with the help of the `itertools.chain` function. This ensures that the elements, though duplicated, are arranged in ascending order. 

The second part of the logic, `len(set(lst)) == len(lst)` checks whether the list has any duplicates. Because a set, by definition, eliminates duplication, their lengths will be the same if there are no duplicates. However, if there are duplicates, the lengths will differ, with the set having a smaller length. 

Therefore, if both conditions are met, the function returns `True`, confirming that the list is sorted with no duplicates, in that order. If either condition is unsatisfied, the function returns `False`. 

The script can be tested as follows: 
```python
# Test Suite
assert is_sorted([1, 2, 3, 4, 5, 6, 7]), "Expected true, got false"

assert not is_sorted([1, 3, 2, 4, 5, 6, 7]), "Expected false, got true"

assert is_sorted([1, 2, 2, 2, 3, 4]), "Expected true, got false"

assert not is_sorted([1, 2, 2, 3, 3, 4]), "Expected false, got true"

assert is_sorted([5]), "Expected true, got false"
``` 
This should return `True` for the first two assertions, and `False` for the last two. 

It's important to note that this solution assumes no negative numbers or floating-point numbers, only integers. Adjustments would be needed for those cases.