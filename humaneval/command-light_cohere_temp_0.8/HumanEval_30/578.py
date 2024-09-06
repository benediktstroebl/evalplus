```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Tests
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(input_list))  # expected output: [5, 3, 2, 3, 9, 123, 1]
input_list = [1, 2, -10, -100, -5000, -20]
input_str = "This is a list: " + input_list
print(input_str)  # expected output: This is a list: [-10, -100, -5000, -20]
```
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It utilizes list comprehension and filtering technique to accomplish this. The test section shows how the process is used to create the output for different scenarios.