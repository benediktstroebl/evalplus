```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  This script defines a function unique that takes a list as an argument and returns a new list containing only the unique elements from the original list. The test_unique function contains a assert statement that checks the correctness of the unique function by passing a known test case.