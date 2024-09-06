```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a simple case
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)

# Test the function with a custom list
numbers_custom = [1, 2, 3, 4, 5]
delimiter = 6
result_custom = intersperse(numbers_custom, delimiter)
print(result_custom)
``` 
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the elements of the original list separated by the specified delimiter. The test cases demonstrate how the