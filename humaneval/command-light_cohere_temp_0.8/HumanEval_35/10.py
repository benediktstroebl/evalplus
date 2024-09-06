```python
def max_element(l: list):
    """Return maximum element in the list
    >>> l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    >>> max_element(l)
    123
    >>> l = [1, 2, 3, 4, 5]
    >>> max_element(l)
    5
    >>> l = [0, 0, 0]
    Traceback (most recent call last):
      File "<stdin>", line 37, in <module>
    ZeroDivisionError: division by zero
    """

    # first case, list is empty
    if not l:
        return 0

    # check for negative elements
    if all(x < 0 for x in l):
        return min(l)

    # find the max element
    max_element = max(l)

    return max_element
```