Here's a Python script that solves the given problem with an efficient approach using `collections`:
```python
from collections import *

def pluck(arr):
    # Your code here!
    even, index = min(zip(arr, range(len(arr))), key=lambda x: (x[0] % 2, x[1]))
    return [even, index] if even else []
```
This approach utilizes the `collections.min` function with a custom `key` argument to find the minimum value and its index, filtering for even values using a lambda function `.lambda x: (x[0] % 2, x[1])`. The lambda function monitors the modulo of even values and their respective indices. This allows the function to efficiently pluck the node with the smallest even value and smallest index from the array when such a node exists, or an empty list when no even values are found. 

Here is a code block incorporating the unit tests to verify the correct functionality of the pluck function:
```python
def test_pluck_function():
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([1, 2, 3]) == [2, 1]
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([7, 3, 9, 1, 5]) == [2, 3]
    assert pluck([0, 7, 2, 1]) == [0, 0]
    assert pluck([10, 8, 4, 12, 6, 14]) == [4, 5]
    assert pluck([13, 2, 11, 7, 3]) == [2, 1]
    assert pluck([0, 0, 2, 4, 6, 8]) == [0, 1]
    assert pluck([3, 10, 8, 12, 9, 5]) == [8, 4]
    assert pluck([2, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [2, 1]
    assert pluck([0, 0, 4, 8, 10, 12, 14, 16, 18, 20]) == [0, 1]
    assert pluck([21, 19, 23, 9, 11, 15, 7]) == [7, 2]
    assert pluck([0, 1, 3, 5, 7, 9, 11, 13, 15, 17]) == [0, 0]
    assert pluck([10, 8, 4, 12, 6]) == [4, 5]
    assert pluck([2, 7, 1, 3, 9, 11, 13, 15, 17, 19]) == [2, 1]
    assert pluck([0, 0, 2, 4, 6, 8]) == [0, 1]
    assert pluck([]) == []
    assert pluck([0, 0, 4, 8, 10, 12, 14, 16, 18, 20]) == [0, 1]
``` 

Ensure that the `test_pluck_function` is called to check if the `pluck` function is operating correctly and ensure its accuracy and compatibility with the problem description.  This can be achieved through the test harness `pytest`.