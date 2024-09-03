```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
        return result
    ``` 
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
test_unique()
 ``` 
This script defines a function unique that sorts and returns unique elements from an input list. It also provides a unique() function a test case to ensure its correctness.