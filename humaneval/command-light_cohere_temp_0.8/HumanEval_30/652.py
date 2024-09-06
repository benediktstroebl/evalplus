```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

# Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
should_positive = get_positive(input_list1)
print("Should be positive:", should_positive)

input_list2 = [5, 3, -2, 99, -5, -20]
should_positive2 = get_positive(input_list2)
print("Should be positive:", should_positive2)

input_list3 = [5, -5, -20, 3, 7]
should_positive3 = get_positive(input_list3)
print("Should be positive:", should_positive3)
```

This code defines a function `get_positive` that accepts a list of numbers and returns a new list containing only the positive numbers. The script also includes a test cases, which pass the function with three different lists of numbers and display the resulting lists to verify the correctness of the `get_positive` function.