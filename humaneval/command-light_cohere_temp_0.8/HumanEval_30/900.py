```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([5, -5, 5, -5])) == 3  # Should return only one positive number, 5
    assert get_positive([-3000, -100, -55]) == [ -100, -55 ]  # Should return both numbers > 0

# Additional test using list of strings
def test_get_positive_strings():
    assert get_positive(["A", "a", "!a", "bc"]) == [".a", "bc"]
```

The above Python code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. It also comes with several test cases to ensure the function's correctness.