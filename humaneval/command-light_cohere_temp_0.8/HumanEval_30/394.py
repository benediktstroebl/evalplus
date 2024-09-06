```python
def get_positive(input_list):
    return [x for x in input_list if x > 0]

# Test case 1
input_list = [-1, 2, -4, 5, 6]
result = get_positive(input_list)
assert result == [2, 5, 6]

# Test case 2
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(input_list)
assert result == [5, 3, 2, 3, 9, 123, 1]
```
This Python script defines a function `get_positive` that takes an input list and returns a new list with only the positive elements. It achieves this task using a simple and efficient filtering using list comprehension and assertion for testing.