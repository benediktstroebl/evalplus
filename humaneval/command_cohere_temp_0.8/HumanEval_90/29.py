```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script defines a function `next_smallest` that takes in a list of integers as an argument. It sorts this list in ascending order using the `sort()` method, and then checks whether the length of the list is less than 2. If the list contains fewer than 2 elements, it returns `None`, indicating that there is no second-smallest element. Otherwise, it returns the second element from the sorted list, which is the second-smallest element in the original list.

Here is a simple unit test for the function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
```