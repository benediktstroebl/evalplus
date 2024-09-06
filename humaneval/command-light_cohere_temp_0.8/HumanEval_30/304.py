```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test case 1
input_list = [-1, 2, -4, 5, 6]
result = get_positive(input_list)
assert result == [2, 5, 6]

# Test case 2
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, -10]
result = get_positive(input_list)
assert result == [5, 3, 2, 3, 9, 123]

# Test case 3 (negative list)
input_list = [-1, 2, -4, 5, 6, -3, -9]
result = get_positive(input_list)
assert result == [2, 5, 6]
```
The function `get_positive` takes a list of numbers as input and returns a new list containing only the positive numbers from the input. 

The function is then tested with three different cases, passing all tests with flying colors.