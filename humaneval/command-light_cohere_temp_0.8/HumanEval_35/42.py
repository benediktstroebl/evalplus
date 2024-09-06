```python
def max_element(lst):
    if not_elements(lst):
        return None
    return max(lst, key=lambda x: x)

def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

def not_elements(lst):
    return not all(map(lambda x: x != 0, lst))

# Run the function tests to ensure the function works correctly
test_max_element()
```