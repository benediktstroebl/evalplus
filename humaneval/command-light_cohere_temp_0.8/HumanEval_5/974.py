```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs and expected outputs
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 5, 8, 16]
result = intersperse(numbers, delimiter)
assert list(expected) == result

# Test with empty list
numbers = []
result = intersperse(numbers, 10)
assert result == []
```