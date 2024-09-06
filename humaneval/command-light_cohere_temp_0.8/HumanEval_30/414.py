```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of numbers
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
# add more tests as needed
```
The function get_positive takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. 
The test code includes two assertions that verify the correctness of the function by checking if the resulting lists match expected values.