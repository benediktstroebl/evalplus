```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of the input list.
    :param numbers: List[int] - list of integers.
    :param delimeter: int - delimiter to insert
    :return: List[int] - list with every integer surrounded by the delimiter
    """
    return [num + delimeter for num, delim in zip(numbers, delimeter * 2)]

# Test cases
numbers = [1, 2, 3,4,5]
print(intersperse(numbers, delimiter =3))
# Expected output: [1,3,2,4,5]

numbers = [1,2,3,4,5,6]
print(intersperse(numbers, delimiter = 6))
# Expected output: [1,2,3,4,6,5]

numbers = [1,2,3]
print(intersperse(numbers, 10))
# Expected output: [1,12,13]

numbers = [1,2,3,4,5,6,7]
print(intersperse(numbers, 2))
# Expected output: [1,2,4,5,6,7]
``` 
This Python code defines a function `intersperse` that inserts a specified delimiter between every two consecutive elements in a given list. It utilizes a
the `zip` function to iterate over pairs of adjacent elements in the list, and adds the delimiter between them. 

The function is then tested with different input lists and different delimiters.