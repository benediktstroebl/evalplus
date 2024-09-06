```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  The code defines a function named unique that takes a list as input and returns a new list containing only the unique elements from the input list. This is unique list is then it uses a set to keep track of elements that have already been encountered. It iterates through elements that each element is only added to the set if it is not already present. The test_unique function tests this input list and asserts that the result of calling the unique function with this input matches the expected output.