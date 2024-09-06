Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a list of all positive numbers in the input list `l`.

To test this function, you can use the following:
```python
# Test list with only positive numbers
>>> get_positive([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]

# Test list with a mix of positive and negative numbers
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]

# Test list with positive and zero values
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

This demonstrates that the function works correctly for different input lists, returning only the positive numbers. Feel free to modify the tests or ask for further assistance as needed.