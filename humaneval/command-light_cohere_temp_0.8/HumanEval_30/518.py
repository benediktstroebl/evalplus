```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

# Test the function
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Output:", get_positive(input_list))
```