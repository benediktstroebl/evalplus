```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a variety of lists
assertEqual(get_positive([-1, 2, -4, 5, 6]) , [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , [5, 3, 2, 3, 9, 123])
assertEqual(get_positive([]) , [])
assertEqual(get_positive([-123, -23, -65]) , [-123, -23, -65])

# Test the function with a negative list
assertEqual(get_positive([-1,-2,-3]) , [−1, −2])

```
This script defines a function `get_positive` that takes a list as an argument and returns a new list with only the positive elements from the original list.  The uses list comprehension to iterate through the original list and applies the condition to filter out the positive numbers. The test cases cover a following: passing the function to different lists and checking the returned lists against the expected results from the function.