```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: List[int] - list of integers, each isolated by at least two digits.
    :param delimiter: int - delimiter to insert
    :return: List[int] - list of integers with separators between them
    """
    return [num]+[num+delimiter for num in numbers] + [num+delimiter]*(len(numbers)-2)
```