```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_data, test_delimiter)
assert test_result == [1, 4, 2, 4, 3]

test_data2 = [1, 2, 3, 4]
test_delimiter2 = 3
test_result2 = intersperse(test_data2, test_delimiter2)
assert test_result2 == [1, 3, 4, 2, 4]

test_data3 = [1, 2, 3, 4, 5]
test_delimiter3 = 2
test_result3 = intersperse(test_data3, test_delimiter3)
assert test_result3 == [2, 3, 4, 2, 5]
```