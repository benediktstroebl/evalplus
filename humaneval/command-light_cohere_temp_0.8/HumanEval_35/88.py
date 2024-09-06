```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = {
    "Test 1": [1, 2, 3],
    "Test 2": [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    "Test 3": [5, 3, -5, 2, -3, 3, 9, 0, 123],
    "Test 4": [5, 3, -5, 2, -3],
    "Test 5": [-1, 2, 3, -1, -100],
    "Test 6": [100, 2, -100],
}

for test_name, test_data in test_max_element.test_data:
    test_val = max_element(test_data)
    print(f"Test {test_name}: {test_val}")
```
This script defines a function max_element that calculates and returns the maximum element from the input list lst. The test cases provide a list of different lists, and the script then uses the max_element function to find the maximum element from each test case and prints the result.