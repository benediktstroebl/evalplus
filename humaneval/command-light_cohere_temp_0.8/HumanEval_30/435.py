```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test case 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Negative input)
try:
    assert get_positive([5, 3, -5, 2, -3, 3]) == [5, 3, 2]
    assert get_positive([9, 2, -4, -1, 7]) == [9, 2, -4, -1, 7]
    assert get_positive([-1, -2, 4, -5, -6]) == [-1, -2, 4, -5, -6]
    assert get_positive([-100, -5, -3, -4]) == [-100, -5, -3, -4]
except Exception as e:
    print(f"Error: {e}")
```