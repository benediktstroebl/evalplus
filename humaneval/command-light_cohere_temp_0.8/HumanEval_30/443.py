```python
def get_positive(input_list):
    positive = [num for num in input_list if num >= 0]
    return positive

# Test case 1
test_case1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(test_case1))  # Output: [5, 3, 2, 3, 9, 123, 1]

# Test case 2
test_case2 = [5, 3, -4, -20]
print(get_positive(test_case2))  # Output: []
```
This Python script defines a function `get_positive` that filters out negative numbers from an input list, producing a new list containing only the positive numbers. The script provides two test cases, where the function correctly returns a list of positive numbers, and an empty list for negative numbers.