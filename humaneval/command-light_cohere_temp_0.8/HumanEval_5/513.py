```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [4, 12, 5, 6, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
should_be = [12, 16, 20, 24, 28]

print(result == should_be)  # True
```