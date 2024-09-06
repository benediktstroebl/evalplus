```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1) + numbers

# Test the function
numbers = [1, 2, 3]
delimiters = [4,] * 3
solution = intersperse(numbers, delimiters)

# Validate the output using tests
assert(solution == [1, 4, 2, 4, 3])
assert len(solution) == 7  # Should be 7, not 8
```