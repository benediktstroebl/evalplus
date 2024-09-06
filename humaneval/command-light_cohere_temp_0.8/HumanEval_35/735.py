```python
def max_element(lst):
    if not_list(lst):
        raise ValueError("Input must be a list")
    return max(lst)

# Test the function with different inputs
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_result = max_element(test_data)
print("Test 1: Result", test_result)

# Test the function with empty list
empty_list = []
test_result2 = max_element(empty_list)
print("Test 2: Result", test_result2)

# Test the function with negative numbers
negative_numbers = [-5, -10, -100]
test_result3 = max_element(negative_numbers)
print("Test 3: Result", test_result3)
```
This Python script defines a function `max_element` that finds the maximum element in a given list. The function raises a error if the input is not a list, and returns the maximum value of the list using the `max()` function. The script then tests this function with three different inputs, printing the results.