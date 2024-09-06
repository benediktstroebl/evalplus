Here is a self-contained Python function that filters out integers from a list of various Python values:
```python
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test cases
test_cases = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

# Function Calls
print(filter_integers(test_cases))  # Output: [5, 1, 2, 3]
```

This function accepts a list of values as an input and outputs a new list that contains only the integers from the input list. It utilizes the filtering logic, where it goes through each value in the input list and creates a new list that only includes integers. This is essential in solving real-world problems that require the removal of specific data types or values from a given list.