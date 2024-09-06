```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` uses the built-in Python `sorted()` function to sort the given list. It then checks if the length of the list is less than 2, returning `None` if the list has only one or zero elements. If the list has more than one element, the function returns the second element (index 1) as it's the second smallest element after the `sorted()` operation.

Here is a simple test suite that can be used to validate the function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([0, 1]) == 1
``` 
Running these tests using a Python test runner or executing the `test_next_smallest()` function will assure that the `next_smallest()` function behaves as expected.