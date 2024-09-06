```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a list of integers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
assert len(result) == 6, "The length should be 6"
assert list(map(result.count, (0, 1, 2, 3, 4, 5))) == 5, "The count should be 5"

# Test another case where list is empty
empty_numbers = []
result = intersperse(empty_numbers, delimiter)
assert len(result) == 0, "The length should be 0"
```