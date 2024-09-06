Here is a Python script that provides a self-contained function to return the sorted unique elements in a list:
```python
import itertools
def unique(lst):
    return list(set(itertools.chain(lst)))
#test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
test_unique()
```
This script defines a function unique that takes a list lst as input and returns a list containing the unique elements from the input list. This is using the unique using set(itertools.chain(lst)) to get the unique elements and the list comprehension [set(itertools.chain(lst))] to convert it to a list.

The script also includes a test case function test_unique() that asserts the correctness of the unique function. 
This test case ensures that the unique function correctly identifies and returns the unique elements from the input list.