```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print(get_positive(test_get_positive))

``` 
This script defines a function called `get_positive` which takes a list as input and returns a new list containing only the positive elements from the original list.  The tested against this expected output of this function using the `push` method to create test cases.