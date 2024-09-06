Here's the self-contained Python function that solves the problem you described:
```python
def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [element for element in values if element.isdigit()]

```

The function accepts a list of any Python value and returns a new list containing only the integer elements from the input list. The test cases are provided to ensure the correctness of the filter_integers function.