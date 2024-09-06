```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    result = [num] + [num + delimeter for num, delimeter in zip(numbers, [0, delimeter])] + [num]
    return result
# Tests
numbers = [1, 2, 3]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3]

numbers = [10, 20, 30]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
assert list(result) == [10, 10, 20, 4, 30, 10, 20, 30]

```