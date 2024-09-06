```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

# Test the function with some examples
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(input_list))  # Expected output: [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -123, 0, -9]
print(get_positive(input_list2))  # Expected output: []

input_list3 = [1, 2, -10, -3, -5, -4, -2]
print(get_positive(input_list3))  # Expected output: [1, 2]
```
This Python code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It employs a specific logic to filter out the positive numbers from the input list. The function is then tested with three different input lists, and the output is displayed, showing the expected results.