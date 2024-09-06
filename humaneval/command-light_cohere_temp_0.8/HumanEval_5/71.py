```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 4, 8]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 8, 2, 12, 3]
```