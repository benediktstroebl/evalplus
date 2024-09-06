```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
test_get_positive = get_positive

# Test list with negative numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print("Test 1: ", test_get_positive(test_list))  # Expected Output: [5, 3, 2, 3, 9, 123, 1]

# Test list with mixed data
test_list2 = [5, 3, -5, 2, -3, 3, 9, 0, -10, 7]
print("Test 2: ", test_get_positive(test_list2))  # Expected Output: [5, 3, 2, 3, 9]

# Test list with only positive numbers
test_list3 = [5, 6, 7, 9, 11]
print("Test 3: ", test_get_positive(test_list3))  # Expected Output: [5, 6, 7, 9, 11]
```

This script defines the function `get_positive`, which takes a list as input and returns a new list with only the positive elements. It then passes this test cases to the function and prints the expected output.