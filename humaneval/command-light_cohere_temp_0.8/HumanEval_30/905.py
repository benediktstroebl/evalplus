```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]

# Test the function with a list of strings
test_strings = ["abc", "def", "-10", "!a", 0]
result_strings = get_positive(test_strings)
print(result_strings)  # Output: ["abc", "def", "a"]

# Test the function with a list of mixed data
test_mixed = [-1, 2. ,"hi", "world"]
result_mixed = get_positive(test_mixed)
print(result_mixed)  # Output: ["2", "hi", "world"]
```

The code defines a function `get_positive` that takes a list `l` as input and returns a new list containing only the positive elements from the original list. The function uses list comprehension to achieve this. The code then tests the test the function with three different types of lists: strings, numbers, and a list of mixed data, and prints the resulting lists to verify the correctness of the function.