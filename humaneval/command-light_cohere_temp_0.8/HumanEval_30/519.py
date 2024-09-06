```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with some lists
print(get_positive([-1, 2, -4, 5, 6]))        # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```
This function get_positive takes a list as input and returns a new list containing only the positive elements from the original list. It utilizes list comprehensions and the `[]` to iterate over each element in the list and check if the element is greater than or equal to zero.