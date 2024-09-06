```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list comprehension to efficiently filter out duplicates and sort the remaining unique elements. The resulting function is concise and effective, providing the desired output for the given problem statement.

Here's an example of how you can use the function unique() to test it:
```python
def test_unique():
    # Test basic case
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Test with single element
    assert unique([1]) == [1]

    # Test with empty list
    assert unique([]) == []

    # Test with unique elements
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

test_unique()
```

The test_unique function employs Python's assert statement to verify that the unique function produces the expected outputs for various test cases. These tests cover a range of scenarios, from lists with duplicates to empty lists and already unique elements, ensuring that the function performs as expected across the board.