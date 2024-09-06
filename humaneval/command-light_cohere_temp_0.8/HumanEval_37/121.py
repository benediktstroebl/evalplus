```python
def sort_even(lst):
    # Sort the list in ascending order
    lst[:]sort()
    even = [x for x in lst if x % 2 == 0]
    even.sort()
    return even
# assert list(even) == [2, 4, 6, 5]
```