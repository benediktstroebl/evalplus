```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list.
    :param numbers: List[int] - list of integers, each represented as an integer.
    :param delimeter: int - Insert a number between every 2 consecutive elements in numbers.
    :return: List[int] - list of integers, each with a delimiter inserted between every 2 consecutive elements.
    """
example: >>> intersperse([1,2,3],4)[
    [1, 4, 2, 4, 3]
    """
    numbers = [x for x in numbers if type(x) == int] 
    return numbers + [delimiter] + numbers[-1:]  # insert at both ends of list
```