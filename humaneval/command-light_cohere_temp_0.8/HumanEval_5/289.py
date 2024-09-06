```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs and expected outputs
numbers = [4, 1, 2, 3]
delimiter = 4
expected = [4, 8, 12, 16]
result = intersperse(numbers, delimiter)
assert len(result) == len(expected)
assert result == expected
```