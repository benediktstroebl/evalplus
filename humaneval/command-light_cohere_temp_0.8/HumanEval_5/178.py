```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [([1, 2, 3], 4)]
test_result = intersperse(test_data, test_data[0])
assert test_result == [1, 4, 2, 4, 3]

test_data = [1, 2, 3, 4]
test_result = intersperse(test_data, 4)
assert test_result == [1, 4, 2, 4, 3]

test_data = [1, 2, 3, 4, 5]
test_result = intersperse(test_data, 4)
assert test_result == [1, 4, 2, 4, 5]

test_data = [10, 20, 30]
test_result = intersperse(test_data, 2)
assert test_result == [10, 20, 10, 30, 10, 20, 30]
```