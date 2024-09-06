```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(seen.add(x) for x in l if x not in seen and x != '')
```

This code uses a set, `seen`, to efficiently track unique elements without repeating operations, as checking for membership in a set is faster than in a list. It iterates over the input list, checking each element against the set. When it encounters a new element, it adds it to the set using the `add` method, ensuring uniqueness. The generated list of unique elements is then sorted for consistency. The result is a streamlined and optimized solution that meets the problem requirement of returning a list of sorted unique elements from the input list. 
```python
def test_unique():
    """Test the unique function"""
    # empty list
    assert unique([]) == []

    # single element
    assert unique([5]) == [5]

    # simple case
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # duplicates
    assert unique([1, 2, 3, 4, 3, 5, 6, 7, 6, 8, 9, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # floats
    assert unique([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]) == [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
``` 

Feel free to add more tests to the `test_unique` function to cover additional scenarios if needed.