```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function `next_smallest()` uses the built-in Python `sorted()` function to sort the given list of integers. Subsequently, the function checks if the length of the list is less than 2. If so, return `None` since the list lacks a second smallest element. Otherwise, the function returns the second element of the sorted list, which is the second smallest element of the original list.

Here is a simpler alternative solution using Python's `min()` function:
```python
def next_smallest(lst):
    return min(set(lst) - {min(lst)} )
```
In this version, the `set()` function removes duplicates, and `min()` returns the smallest element. This approach avoids sorting while achieving the same result.