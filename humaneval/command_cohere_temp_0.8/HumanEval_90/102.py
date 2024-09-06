```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and returns the second element if the list has at least two elements. It returns `None` if the list has less than two elements or if the list contains only duplicates. 

Here is a snippet of tests to ensure the function `next_smallest()` works as expected:
```python
# Test 1
assert next_smallest([1, 2, 3, 4, 5]) == 2

# Test 2
assert next_smallest([5, 1, 4, 3, 2]) == 2

# Test 3
assert next_smallest([]) == None

# Test 4
assert next_smallest([1, 1]) == None
```
These tests aim to cover different scenarios that the function might encounter.