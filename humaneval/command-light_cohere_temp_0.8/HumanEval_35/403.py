```python
def max_element(lst):
    if not_unique(lst):  # Check for empty list or contains duplicates
        raise ValueError("Input list must be unique")
    return max(lst)

def test_max_element(test_lst):
    assert max_element(test_lst) == 3  # Test with known values

# Test with a list of various data types
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_data)

test_empty = []
test_max_element(test_empty)
``` 
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. By doing a dry runs and tests using the code.