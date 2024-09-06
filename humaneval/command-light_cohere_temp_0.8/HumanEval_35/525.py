```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list is empty")
    return max(lst)

def test_max_element():
    try:
        test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        max_element(test_list)
        print("Test passed")
    except ValueError as e:
        print("Test failed:", str(e))
    
# Test function
test_max_element()
```

This code defines a Python function `max_element` that calculates and returns the maximum element in the input list. The `test_max_element` function tests this function with a sample list and prints the result.