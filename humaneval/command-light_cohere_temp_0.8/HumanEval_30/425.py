```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test the function with a list of different types of numbers
test_func = get_positive([-1, 2, -4, 5, 6])
test_func.assert test_list([-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

# Validate the output
print(test_func == [5, 3, 2, 3, 9, 123, 1])  # True
```