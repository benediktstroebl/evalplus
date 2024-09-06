```python
def filter_integers(values): 
    return [i for i in values if isinstance(i, int)]

# Test cases 

test_values = [ ['a', 3.14, 5, 1, 2, 'abc', {}, []]

test_results = filter_integers(test_values)

assert all(test_results) == [5]

test_empty_values = [1, 2, 3, 'abc', {},]

test_results2 = filter_integers(test_empty_values)

assert test_results2 == []

test_invalid = ['a', 3.14, 'abc]

with pytest.assert expected=[]:
    test_results3 = filter_integers(test_invalid)
    assert test_results3 == []
```