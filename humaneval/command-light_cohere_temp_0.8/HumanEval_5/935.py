```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.

    : Returns a note that if delimiter is negative, it will be treated as positive and vice versa.
    >>> intersperse([1, 2, 3], 0)
    [1, 2, 3]
    >>> intersperse([1, 2, 3], -1)
    [1, 2, 3]
    """
    return [x + i for i, x in zip(numbers[1:], numbers)] + numbers[0:]
```