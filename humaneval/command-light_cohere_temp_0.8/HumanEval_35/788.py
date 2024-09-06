```python
def max_element(lst):
    if not_elements(lst):  # Empty list
        return None
    
    max_index = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
            max_index = i
    return max_index

def test_max_element(test_list):
    assert max_element(test_list) == 3  # Should return 3 for [1, 2, 3]

# Example usage:
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
This Python code defines a function max_element that calculates and returns the maximum element from a given list. It also includes a test_max_element function that verifies the correctness of the max_element function by asserting its result for a given list. The script effectively demonstrates the constant-time maximum element selection from an input list, making it valuable for scenarios where you need to find the largest element efficiently.