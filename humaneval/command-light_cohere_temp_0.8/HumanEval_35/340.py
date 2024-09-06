```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function
def test_max_element():
    try:
        result = max_element([1, 2, 3])
        assert result == 3
        result = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        assert result == 123
        return True
    except AssertionError as e:
        print(f"Error: {e}" )
        return False

result = test_max_element()
print(result)
```