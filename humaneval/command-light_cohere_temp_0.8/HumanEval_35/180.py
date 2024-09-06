```python
def max_element(lst):
    if not_elements(lst):  # Base case
        return None
    max_ = lst[0]  # Initialize with first element
    for num in lst[1:]: 
        if num > max_:
            max_ = num 
    return max_

def test_max_element(test_list): 
    test_result = max_element(test_list)
    assert max_result is not None, "Test case failed."  # Base case check
    for item in test_list: 
        assert item <= max_result, f"Test case {item} failed" 
    return True 

# Main code
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_result = max_element(test_data)
print("Test passed:", test_result)  # This will print the max_result
```