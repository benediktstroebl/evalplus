```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    # Initialize the maximum element to the first element of the list
    max_el = l[0] if l else None

    # Iterate through the list and update the maximum element if a larger value is encountered
    for el in l:
        if el > max_el:
            max_el = el

    return max_el
``` 

The function `max_element` takes a list `l` as input and returns the maximum element in the list. The function initially sets the maximum element to the first element of the list. It then iterates through the list, comparing each element to the current maximum element. If an element is greater than the current maximum element, it is updated to the new maximum element. 

Here is an example of using the max_element function:
```python
max_element([1, 2, 3])
# Output: 3

max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Output: 123
``` 

The function will return the maximum element in the list, ignoring any negative values. However, it is worth noting that including negative values in the input list may result in unexpected behavior from the function due to the initial maximum element set to the first element, which, in most cases, will be a positive value, and the comparison of the elements to the maximum will mostly be concerned with finding the maximum positive value.