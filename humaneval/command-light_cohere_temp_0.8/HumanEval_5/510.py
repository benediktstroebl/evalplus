```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n + delimeter)
    return result

# Test the function with sample inputs
test_data = [1, 2, 3]
test_result = intersperse(test_data, 4)
assert test_result == [1, 4, 2, 4, 3]

test_data2 = [1, 2, 3, 4]
test_result2 = intersperse(test_data2, 4)
assert test_result2 == [1, 4, 2, 4, 3, 4]

# Test with empty list
test_data3 = []
test_result3 = intersperse(test_data3, 4)
assert test_result3 == []
```