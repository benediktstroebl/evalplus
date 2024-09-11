### Monotonic List Checker
#### Problem Statement
Return `True` if list elements are monotonically increasing or decreasing.

#### Solution
```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        # Check if list is increasing
        if l[i] < l[i - 1]:
            increasing = False
        # Check if list is decreasing
        if l[i] > l[i - 1]:
            decreasing = False

    return increasing or decreasing
```

#### Explanation
This function takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing. It initializes two flags `increasing` and `decreasing` to `True` and then iterates over the list from the second element to the end. If it finds an element that is smaller than its previous element, it sets `increasing` to `False`. Similarly, if it finds an element that is larger than its previous element, it sets `decreasing` to `False`. Finally, it returns `True` if either `increasing` or `decreasing` is still `True`, indicating that the list is either increasing or decreasing.