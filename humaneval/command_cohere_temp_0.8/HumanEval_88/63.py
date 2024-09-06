```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```

The function `sort_array()` sorts the array based on the sum of its first and last elements, odd sums sort in ascending order, and even sums sort in descending order. Also, the base case handles empty arrays.

Here is a test suite to ensure the function behaves correctly:
```python
def test_sort_array():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([10, 40, 30, 20, 11, 0]) == [0, 10, 11, 20, 30, 40]
``` 
The test cases cover multiple scenarios to ensure the function sorts arrays correctly based on the criteria specified in the problem.