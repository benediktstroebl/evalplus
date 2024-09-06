```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 ( Edge case:List with one element )
assert max_element([9]) == 9
``` 
This code defines a function max_element that takes a list lst as input and returns the maximum element in the list. It uses the particular Python's max() function to get the maximum element from the list.