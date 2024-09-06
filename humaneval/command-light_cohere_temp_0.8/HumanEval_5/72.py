```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a list of integers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
assert len(result) == len(numbers) + 2*delimiter

# Test the function with empty list
numbers = []
result = intersperse(numbers, 10)
assert len(result) == 0

# Test the function with one number
numbers = [1]
result = intersperse(numbers, 10)
assert len(result) == 11

# Test the function with invalid delimiter (zero)
numbers = [1, 2, 3]
delimiter = 0
with pytest.assert(). assert_raises(ValueError, intersperse, numbers, delimiter)
```