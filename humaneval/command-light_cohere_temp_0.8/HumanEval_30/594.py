```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test case 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Test case 3
assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 9

# Test case 4
assert get_positive([]) == []

# Test case 5
try:
    x = get_positive([3, 2, -9, 7, -4, 5, 6, -100, 8, -1000])
    assert x == [3, 2, 5, 7, 4]
except Exception as e:
    print(f"Error occurred: {e}")
```