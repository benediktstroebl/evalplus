```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    lst = [-1, 2, -4, 5, 6]
    actual = get_positive(lst)
    assert actual == [2, 5, 6]

# Example usage
lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(lst1))
```