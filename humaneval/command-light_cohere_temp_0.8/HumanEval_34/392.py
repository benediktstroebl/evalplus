```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, None]]

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_list():
    assert unique([5, 'abc', 'abc', 123]) == ['abc', 123]

def test_empty_list():
    assert unique([]) == []

def test_none():
    assert unique([None]) == []

if __name__ == "__main__":
    test_unique()
    test_list()
    test_empty_list()
    test_none()
```
This Python script defines a function called `unique` that returns a list of unique elements from an input list. It also comes with a set of unique elements and a series of test cases to verify the correctness of the function.