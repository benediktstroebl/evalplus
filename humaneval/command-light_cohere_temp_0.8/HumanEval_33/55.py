```python
def sort_third(lst):
    return sorted(lst, key=lambda x: (x // 3) % 2 == 0))

# Test the function with some sample inputs
assert(sort_third([1, 2, 3]) == [1, 2, 3])
assert(sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5])
```
This script defines a function `sort_third` that takes a list `lst` as input and returns a sorted list such that elements which are divisible by three are sorted towards the end of the list and all other elements are sorted in ascending order. The function uses the sole key that is a lambda function `(x // 3) % 2 == 0)`, which returns True if the value of `x` is a remainder of `³` divided by `3` and is equal to zero. The list is sorted using this key, which returns a sorted list with elements divisible by three at the end.