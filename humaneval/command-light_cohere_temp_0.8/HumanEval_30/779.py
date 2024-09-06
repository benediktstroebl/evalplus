```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = [
    {'input': [-1, 2, -4, 5, 6],
     'expected': [2, 5, 6]
    },
    {'input': [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
     'expected': [5, 3, 2, 3, 9, 123, 1]
    },
    # Add more test cases here...
]

# Execute the tests
test_get_positive()
```

This Python code defines a function named `get_positive` that takes a list (`lst`) as input and returns a new list containing only the positive numbers from the original list. It employs list comprehension with the distinct logic to filter out the positive numbers.

This function can be efficiently used for any given list, and the output will be the desired list of positive numbers.