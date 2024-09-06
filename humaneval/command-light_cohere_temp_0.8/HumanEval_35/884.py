```python
def max_element(lst):
    if not_list(lst):
        raise ValueError("Input must be a list")
    return max(lst)

# Test the function
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_list)
print("Maximum element:", result)

# Test with invalid input
invalid_input = [42]
try:
    result = max_element(invalid_input)
except ValueError as e:
    print("Error:", e)
```

This code defines a function max_element that finds the maximum element in a list. Using the max() function on the list and checking for the type of the input ensures that only lists are passed as arguments, avoiding potential errors with other data types.