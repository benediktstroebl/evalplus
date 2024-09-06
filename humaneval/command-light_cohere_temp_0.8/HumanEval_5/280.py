```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1)

# Test cases
numbers = [1, 2, 3]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
assert len(result) == 6
assert result[0] == 1
assert result[1] == 4
assert result[3] == 8

numbers = [4,5,6]
delimiters = [1, 2]
result = intersperse(numbers, delimiters)
assert len(result) == 3
assert result[0] == 4
assert result[1] == 1
assert result[2] == 2
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a list with the numbers and the delimiter inserted between consecutive elements. The test cases demonstrate the