```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function unique that takes a list as input and returns a new list containing only the unique elements from the original list using the set() function. The test_unique function contains the test case, which asserts that the result of calling unique with a list of numbers satisfies the expected behavior. 

This code is a good example of a self-contained function with tests that demonstrate its correctness.