Here's the function that solves the problem:
```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

And here's the test code:
```python
def test_unique():
    # Test list
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    
    # Call the unique function
    result = unique(test_list)
    
    # Check the results
    assert len(result) == 7  # All elements should be unique
    assert set(result) == set([0, 2, 3, 5, 9, 123])

test_unique()
```