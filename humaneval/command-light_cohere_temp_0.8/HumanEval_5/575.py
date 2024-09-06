```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 4, 4]
result = intersperse(numbers, delimiters)

print(result == [1, 4, 2, 4, 3])  # Should print True
print(result == [1, 2, 4, 4, 3, 4])  # Should print True
print(result == [1, 2, 4, 8, 3])  # Should print False
``` 
The function `intersperse()` takes a list of integers and a delimiter as input and returns a new list with the elements of the original list separated by the specified delimiter. This implementation uses a