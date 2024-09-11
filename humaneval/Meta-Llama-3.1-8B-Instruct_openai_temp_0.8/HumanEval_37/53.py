### Sorting Even Indices in a List

Here is a Python function that solves the problem:
```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the even and odd indices into different lists
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even list
    even.sort()
    
    # Combine the sorted even list with the odd list
    return [x if i % 2!= 0 else y for i, x in enumerate(odd) for y in even]
```
This function uses list comprehensions to separate the even and odd indices in the input list into different lists, sorts the even list, and then combines the two lists while maintaining their original indices.

You can test this function with the examples you provided:
```python
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```