Here's the function that implements the filtering for integers:
```python
def filter_integers(values):
    """Filter given list for integers."""
    return [x for x in values if isinstance(x, int)]

# Testing the function
values_test = [1, 2, 'three', 3.14, 5]
print(filter_integers(values_test))  # Expected output: [1, 2, 3, 5]
```
The function takes a list of values as input and returns a new list containing only the integers from the input list. It uses the `is filtering approach to identify the elements that are of type `int` and filter out all other types of values from the list.

This function is self-contained and can be used to filter any list of values for integers. It can be easily tested and is a straightforward and efficient way to solve the problem.