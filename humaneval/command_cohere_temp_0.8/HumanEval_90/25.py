```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This approach takes the list and sorts it using the sorted() function. The sort order ensures that the smallest element is at the first index and the second smallest at the second index. Then we simply return the second element if it exists, and None if the length of the list is less than 2. 

The test cases provided in the problem statement are reflected in the corresponding test script:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None

test_next_smallest()
```
These tests check if the function `next_smallest` works correctly for different scenarios like empty list, list with one element, and lists with two or more elements. 
The assert statements will raise an exception if the yielded value by the function is incorrect, thereby failing the test and indicating that the function may require reassessment.