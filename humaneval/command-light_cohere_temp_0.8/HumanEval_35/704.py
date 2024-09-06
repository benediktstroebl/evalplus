```python
def max_element(lst):
    if not_elements(lst):  # Handle empty list
        return None
    
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

def test_max_element(test_list):
    actual_max = max_element(test_list)
    expected_max = [1, 2, 3, 5, 3, -5, 2, -3, 3, 9, 123, 10]
    
    print(f"Test List: {test_list}")
    print(f"Expected Max Element: {expected_max}")
    print(f"Actual Max Element: {actual_max}")
    
    assert actual_max == expected_max, "Elements do not match!"
```