```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)  # Expected output: [1 4 8 2 16 120]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the integers, separated by that delimiter. The test case provided also demonstrates the expected behavior.