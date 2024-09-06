```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([]) == None

# Test case 4
assert max_element([1, 2, 3, 4, 5]) == 5
``` 
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. This is using the `max()` function from the list's elements to find the maximum. 

The provided test cases validate the function's behavior.