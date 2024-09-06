```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
   
    return numbers interposed with the delimiter """

numbers = [1, 2, 3, 4]
print(intersperse(numbers, 4))  # Output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 4))  # Output: [1, 4, 5, 4, 5]

numbers = [10, 20, 30, 40]
print(intersperse(numbers, 10))  # Output: [10, 20, 30, 40]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intersperse(numbers, 10))  # this should produce error: types don't match

```