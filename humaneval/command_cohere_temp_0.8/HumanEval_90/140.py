```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element of the sorted list. Since sorting the list creates a new list, the function modifies the original list. If the list has less than 2 elements, the function returns `None`. 

Here is a test drive suite that can be added to verify the correctness of the function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([0, 0, 0, 4, 5, 6]) == 1
    assert next_smallest([2, 1, 9, 4, 3, 5, 7, 8, 6]) == 1
``` 

You can use the function by calling `test_next_smallest()` to verify the correctness of the `next_smallest` function. 
This way, you can ensure that the function behaves as expected and conforms to the problem statement. 
The order of the tests is random, so you may want to shuffle them for better test coverage.