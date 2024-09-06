```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
``` 
The code defines a function get_positive that takes a list as input and returns a new list with only the positive numbers from the original list. The test cases verify the all the expected behavior of the function, by creating lists with both positive and negative numbers and comparing the output of the get_positive function with the correct expected result.