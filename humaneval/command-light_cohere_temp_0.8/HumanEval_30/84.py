```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)

# Print the result
print(result)

# Test the function with a mixed list
mixed_list = [-1, 2, 5, 3, -4, 0, -123]
result = get_positive(mixed_list)

# Print the result
print(result)
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It is then pass a tests using both a list of only positive numbers and a mixed list with negative and positive numbers.