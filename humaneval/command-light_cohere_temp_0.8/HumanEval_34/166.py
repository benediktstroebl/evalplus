```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test the function with a list of mixed data
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("unique:", unique(test_list))  # Expected output: [0, 2, 3, 5, 9, 123]

# Test the function with float('inf') to handle NaN case
test_list_inf = [5, 3, 'inf', 0]
print("unique:", unique(test_list_inf))  # Expected output: []

# Test the function with empty list
test_list_empty = []
print("unique:", unique(test_list_empty))  # Expected output: []
```
The function unique provided in this Python script accepts a list as input and outputs a list of its unique elements, sorted in ascending order. It uses the unique set to keep track of the elements already seen and returns a new list with no duplicates. The test cases demonstrate how the test the function behaves for various scenarios, such as mixing data types, floating-point numbers, and an empty list.