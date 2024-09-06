```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers (List[int]): list of integers to be interspersed.
        delimiter (int):: Insertion integer.
    Returns: list of integers with the inserted delimiter.
    """
Example:
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [num + i * delimeter for i, num in enumerate(numbers)]
```