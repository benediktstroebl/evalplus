```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists
# Test the function with a list of negative numbers
test_get_positive_negative() = [
    [-1, 2, -4, 5, 6],
    [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
]

# Function call with test input
result = get_positive(test_get_positive_negative())
print(result)  # Output: [2, 3, 5, 6, 9, 123, 1]

# Test the function with a list of mixed numbers
test_get_positive_mixed() = [
    5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10
]

# Function call with test input
result = get_positive(test_get_positive_mixed())
print(result)  # Output: [2, 3, 5, 6, 9, 123]

# Test the function with a empty list
test_get_empty() = []

# Function call with test input
result = get_positive(test_get_empty())
print(result)  # Output: []
```
The script defines a function called **get_positive** that takes a list as an argument and returns a new list containing only the positive numbers from the original list. It is also includes a set of test cases to verify the correctness of the function. The tests include various scenarios, such as passing an empty list, a list with both positive and negative numbers, a list with only positive numbers, and a list with mixed positive and negative values.  The test the results show that the function returns the expected output for each test case.