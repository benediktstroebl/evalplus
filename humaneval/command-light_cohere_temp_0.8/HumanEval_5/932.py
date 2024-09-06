```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    >>> intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    True
    >>> intersperse([1, 2, 3, 4], 5)
    []
    >>> intersperse([1,2,3,4,5],3)
    [1,3,4,5]
    """
    new_list = []
    for item in numbers:
        new_list.append(item)
        if len(new_list) != 1:
            new_list.append(delimiter)
   
    return new_list
```