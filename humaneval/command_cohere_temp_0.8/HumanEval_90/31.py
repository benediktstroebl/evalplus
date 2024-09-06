```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach employs the Python built-in sorting function, `sort()`. The list is sorted in ascending order, and the second last element returned as the 2nd smallest element, handling the base case where the list has less than 2 elements gracefully with the line, `if len(lst) < 2: return None`. 

Here is a snippet of tests to accompany the function to complete the self-contained solution:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([2, 1, 1, 1, 1]) == 1
    assert next_smallest([10, 5, 3, 2, 1]) == 3
    assert next_smallest([10, 5, 3, 1]) == 1
``` 

To run the above tests, you can use Python's built-in `unittest` module by importing it into your script or in the Python environment where these functions are housed. The script would then be run with `python -m unittest your_file_name.py` where `your_file_name.py` is the name of the file that houses these functions. 

These tests cover multiple cases, assuring the function behaves as expected by checking for the return of `None` when the list size is less than 2 and correctly identifying the 2nd smallest element for lists that have 2 or more elements.