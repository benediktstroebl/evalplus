```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in set()]
    # tests
    assert list(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) == [0, 2, 3, 5, 9, 123]
    assert len(unique([5, 6, 7, 5, 5, 8, 5])) == 5  # This is due to 5 being repeated
    assert len(unique([5, 5, 5, 5])) == 1
```  This code defines a function unique that takes a list as input and returns a new list with unique elements from the input list. The seen set keeps track of elements that have been encountered, and the outer loop ensures that elements not in seen and not in the set are added to the result list.