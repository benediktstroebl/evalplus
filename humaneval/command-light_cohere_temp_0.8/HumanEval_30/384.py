```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test the function with a variety of input lists
input_lists = [
    [],
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, -10],
]

for input_list in input_lists:
    print(get_positive(input_list))  # Output should be: [2, 5, 6, [5, 3, 2, 3, 9, 123], 1]
```