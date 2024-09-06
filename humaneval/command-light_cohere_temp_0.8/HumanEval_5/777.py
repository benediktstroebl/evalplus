```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1):  # Start from the second element
        if i % 2 == 0:  # Even index, insert the delimiter
            result.append(delimiter)
        else:
            result.append(numbers[i])
    return result

# Unit tests
test_case1 = [4, 2,3]
test_case2 = [1, 2, 4, 3]
test_case3 = [10, 20, 30, 10, 40]
test_case4 = [1, 4, 2, 4, 3]
test_case5 = [1, 2, 3, 4, 5]
test_result1 = intersperse(test_case1, 4)
test_result2 = intersperse(test_case2, 4)
test_result3 = intersperse(test_case3, 4)
test_result4 = intersperse(test_case4, 4)
test_result5 = intersperse(test_case5, 4)

assert test_result1 == [4, 2, 4, 6]  # Should be [4, 2, 4, 6]
assert test_result2 == [1, 4, 2, 4, 6]  # Should be [1, 4, 2, 4, 6]
assert test_result3 == [10, 20, 24, 28]  # Should be [10, 20, 24, 28]
assert test_result4 == [1, 4, 2, 8, 3]  # Should be [1, 4, 2, 8, 3]
assert test_result5 == [1, 2, 3, 8, 5]  # Should be [1, 2, 3, 8, 5]  # Modify as needed
```