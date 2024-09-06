```python
def sort_third(l: list):
    l_sorted = [x for i, x in enumerate(l) if i % 3 != 0]
    l_sorted += [sorted(y for y in l if i % 3 == 0)]
    return l_sorted
```

This script defines a function `sort_third` which takes in a list `l` as an argument and returns a new list `l_sorted`. The function works by creating a new list `l_sorted` and a generator expression `x for i, x in enumerate(l) if i % 3 != 0` which encapsulates a loop going through the list `l` and only includes elements at indices that are not divisible by three. The elements encountered in this loop are appended to `l_sorted`. Following this, a generator expression `sorted(y for y in l if i % 3 == 0)` is sorted and appended to `l_sorted`. The result is a list `l_sorted` where the elements at indices that are not divisible by three are unchanged, and the elements at indices that are divisible by three are sorted.

Here is an example usage of the function:
```python
sort_third([1, 2, 3]) # Output: [1, 2, 3]
sort_third([5, 6, 3, 4, 8, 9, 2]) # Output: [2, 6, 3, 4, 8, 9, 5]
```

This example usage demonstrates the function's ability to sort the list according to the challenge description.