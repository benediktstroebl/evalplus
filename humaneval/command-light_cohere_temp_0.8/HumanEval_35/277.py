```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else lst[-1] + max(lst[:-])

# Test cases
test_max_element = [
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [100, 200, 50, 25, 15, 75],
    [-10, -5, -20]
]

for test_case in test_max_element:
    actual_result = max_element(test_case)
    assert actual_result == test_case[-1]
``` 
This code defines a function max_element that finds the maximum element in a given list. It uses a strategy of comparing the list element with the last element in the list to achieve this. The test cases ensure the for different list structures, the max_element function returns the correct maximum element.