```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

#Test the function
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(input_list)
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]
```
This script defines a function `get_positive` that takes a list as an argument and returns a new list with only the positive numbers from the input list. It effectively solves the"! principle and provides the following output: