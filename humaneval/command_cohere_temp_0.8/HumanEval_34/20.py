```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The above method uses a set called 'seen' to keep track of unique elements and returns a sorted list of missing elements. 

To correctly solve the task, you may also wish to include a test suite, such as the following:
```python
def test_unique():
    # Test list with duplicate elements
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    
    # Test list with unique elements
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test empty list
    assert unique([]) == []
    
    # Test list with one element
    assert unique([7]) == [7]
```

This test suite covers instances of the 'unique' function with various input contexts. You may use these to validate your function and ensure that it performs as expected, allowing you to solve the problem accurately. 
To run these tests, you can copy and paste the code into a Python environment or IDE. 

Make sure that the expected output is aligned with the problem statement, ensuring that the elements are sorted. Mistakes could lead to incorrect outcomes, so double-check your computations and comparisons.