```python
def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []]
]

test_results = [filter_integers(value) for value in test_values]

print("Test results:", test_results)
``` 
This script defines a function called `filter_integers` that takes a list of values and returns a new list that contains only the integers from the original list. The script then provides a test cases to verify the functionality of the function, and the expected results are printed to the console.