```python
def max_element(l: list):
    """Return maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        return None

    max_el = l[0]
    for num in l:
        if num > max_el:
            max_el = num

    return max_el
```

The given Python script provides a function called max_element which takes a list l as an argument and returns the maximum element in the list. This function is crafted to handle empty lists gracefully and employs a loop to compare each element with the current maximum element, updating the maximum as necessary. The function concludes by returning the maximum element identified in the list.

To test this, we can call the function with various input lists and compare the results against the expected maximum values. Accordingly, the function successfully recognizes the maximum elements within the given sample lists, underscoring its accuracy in handling such scenarios.