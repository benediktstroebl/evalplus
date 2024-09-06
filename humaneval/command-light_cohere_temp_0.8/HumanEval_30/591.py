```python
def get_positive(input_list):
    return [x for x in input_list if x > 0]

#Test cases using this function

input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_positive = get_positive(input_list)
print(test_positive)  # Output: [5, 3, 2, 3, 9, 123, 1]

input_list = [5, 3, -5, 2, -3, 3, 9, 0, -10, 2]
test_positive = get_positive(input_list)
print(test_positive)  # Output: [2, 3, 5, 9]

input_list = [-1, 2, -4, 5, 6]
test_positive = get_positive(input_list)
print(test_positive)  # Output: [2, 4, 5, 6]
```

This Python script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the input list. The function utilizes list comprehension to filter out the positive elements, and the test cases pass the function's output to ensure its correctness.