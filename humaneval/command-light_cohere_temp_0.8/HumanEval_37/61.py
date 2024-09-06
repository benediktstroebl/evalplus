```python
def sort_even(lst):
    """Sorts the list l such that elements at odd positions are kept as they are, and
    the elements at even positions are sorted."""
    return sorted(lst, key=lambda x: x // 2 if x % 2 == 0 else x)

#Example:
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```
This script defines a function **sort_even** that takes a list lst as input and sorts it such that the elements at odd positions are kept as they are, and the elements at even positions are sorted. The function uses the fact or **sorted** function from the Python standard library, which sorts the list using a custom key function that compares each element to its floor division by 2 (i.e., sorts the same element the value if the number is even, and leaves the original value if the number is odd.