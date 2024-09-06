```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]
expected = [1, 4, 8, 2, 12, 3, 16, 5]
print(expected == intersperse(numbers, delimiters))
```