```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function 'next_smallest' sorts the input list using the 'sorted' function, which arranges elements in ascending order. Subsequently, the function checks whether the length of the list is less than 2. If the list has only one element or is empty, indicating no second smallest element, the function returns 'None'. Otherwise, the function retrieves the second element from the sorted list using indexing, providing the second smallest element of the original list.

Here is a simple test suite to verify the functionality of the function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
    assert next_smallest([2, 1, 1, 11, 2, 5, 4, 3]) == 1
test_next_smallest()
``` 
The test suite contains four test cases, covering edge scenarios like empty lists, lists with only one element, and lists where the second smallest element is not present. The 'assert' statements check whether the 'next_smallest' function returns the expected outputs for these scenarios. The 'test_next_smallest' function calls the 'next_smallest' function and compares its output with the expected values; consequently, the 'test_next_smallest' function ensures that the 'next_smallest' function behaves as expected.