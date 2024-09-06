```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_numbers = [([1, 2, 3], 4), [5, 6], [7, 8])

for test_set in test_numbers:
    expected = [1, 4, 2, 4, 3, 8]
    actual = intersperse(test_set, 4)
    assert actual == expected, f"Failed for test set: {test_set}"
```  It takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by that delimiter.