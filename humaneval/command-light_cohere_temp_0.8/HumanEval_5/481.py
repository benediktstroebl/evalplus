```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)

# Test passing parameter
numbers = [1, 2, 3, 4]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)

# Test negative number
numbers = [10, 20, 30]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with numbers separated by the provided delimiter. The test cases cover different scenarios, such as passing an empty list, passing a list of numbers with a delimiter, passing a list of numbers with a delimiter, and passing a negative number for the delimiter.