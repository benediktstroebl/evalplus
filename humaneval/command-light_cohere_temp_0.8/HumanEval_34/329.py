```python
def unique(lst):
    return list(set(lst))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
``` 
This code defines a function unique that returns a list of unique elements from an input list. The test_unique function contains a assertion that verifies the correctness of the unique function.