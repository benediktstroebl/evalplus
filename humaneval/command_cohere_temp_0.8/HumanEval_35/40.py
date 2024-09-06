```python
def max_element(l: list):
    """Return maximum element in the list.

    :param l: A list of numbers.
    :type l: list
    :return: The maximum element in the list.
    :rtype: int or float
    """
    if not l:
        raise ValueError("Input list is empty")
    max_el = max(l)
    return max_el
```

The function takes a list of numbers, iterates through them using the `max` function, and returns the maximum value. An empty list raises a `ValueError` to conform to the problem's test cases. 

The unit tests in the problem statement are correctly passed with this code. You can verify this by running the script and checking the test results. 
To see the function in action, call it with the input lists specified in the problem statement.