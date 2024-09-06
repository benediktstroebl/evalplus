```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(input_list))
```