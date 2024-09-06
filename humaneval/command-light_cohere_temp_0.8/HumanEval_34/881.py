```python
def unique(lst):
    return list(set(lst))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function unique that returns the unique elements of the input list lst by using the set() function to remove duplicate elements and the list() function to convert the set to a list.

Then the code defines a test function test_unique that tests the unique function by passing the test list and asserting that the result is the expected unique elements list.