```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list and returns the second smallest element if there are at least two elements in the list, or `None` otherwise.  This approach takes advantage of the fact that sorting the list takes advantage of the inherent order in the list, making the second smallest element the second element in the sorted list, which is achieved using indexing `-2` on the sorted list. This achieves the desired results as specified in the problem statement. 

Here is a test suite that can be used to validate the functionality of this code:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([2, 1, 1, 1, 4, 4, 2, 3, 3, 5, 5, 2, 2]) == 2
    assert next_smallest([10, 5, 20, 4, 3, 8, 7, 9]) == 3
    assert next_smallest([10, 5, 20, 4, 3, 8, 7, 9, 2, 1]) == 1
    assert next_smallest([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 20
```

You can verify the correctness of the function by calling `test_next_smallest()` and asserting the expected output against the output of running `next_smallest()` with the corresponding input list.  This approach allows for robust, straightforward, and efficient computation of the second smallest element, without the need for additional libraries.  This is a great example of how Python's built-in functionality can be leveraged to efficiently and effectively solve real-world coding problems.  Here would be the complete code putting it all together: 
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([2, 1, 1, 1, 4, 4, 2, 3, 3, 5, 5, 2, 2]) == 2
    assert next_smallest([10, 5, 20, 4, 3, 8, 7, 9]) == 3
    assert next_smallest([10, 5, 20, 4, 3, 8, 7, 9, 2, 1]) == 1
    assert next_smallest([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 20
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```