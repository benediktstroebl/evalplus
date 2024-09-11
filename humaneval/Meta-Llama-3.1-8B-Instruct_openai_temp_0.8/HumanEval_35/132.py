### Maximum Element in a List
#### Description
This script defines a function `max_element` that takes a list as input and returns the maximum element in the list.

#### Code
```markdown
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    l (list): Input list.
    
    Returns:
    The maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
#### Explanation
This script uses the built-in `max` function in Python to find the maximum element in the list. The `max` function takes an iterable as input and returns the largest item in the iterable. In this case, we pass the input list `l` to the `max` function, which returns the maximum element in the list. 

Note that this implementation has a time complexity of O(n), where n is the length of the input list, because the `max` function needs to iterate over the entire list to find the maximum element.