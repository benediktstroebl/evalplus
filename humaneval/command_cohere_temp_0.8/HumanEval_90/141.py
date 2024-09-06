```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list and returns the second smallest element if there are at least two elements in the list, or `None` otherwise. 

Here is a snippet of tests to ensure the function works as expected:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None

test_next_smallest()
``` 
This will ensure that the function `next_smallest` behaves as expected.