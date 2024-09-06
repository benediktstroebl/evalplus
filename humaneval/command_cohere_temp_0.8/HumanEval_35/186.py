```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    # initialize maximum element
    max_el = float('-inf')

    # iterate through the list and update maximum element if necessary
    for x in l:
        if x > max_el:
            max_el = x

    return max_el
``` 

The function 'max_element' takes a list `l` as an argument and returns the maximum element in the list. To ensure that the maximum element is correctly updated, the variable 'max_el' is initialized to negative infinity (`float('-inf')`). As the function iterates through the list, if it encounters an element greater than the current maximum element, it updates the 'max_el' variable. 

Here's an example usage of the function:
```python
print(max_element([1, 2, 3]))  # Outputs: 3
```

And here's another example:
```python
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Outputs: 123
```

This will return the maximum element in the list, which in this case is 123. 

The code is self-contained and does not rely on external variables or functions. It also doesn't change the original list, which makes it safe and easier to reuse for other lists.