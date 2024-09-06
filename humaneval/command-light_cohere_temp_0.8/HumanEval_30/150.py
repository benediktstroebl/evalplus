```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([9, 5, -5, -20])
    assert not get_positive([down_for_now])

# Call the function with test data
down_for_now = [-2, -3, -100]
print(f"Result: {down_for_now}")
```  # this will print: Result: [-100]