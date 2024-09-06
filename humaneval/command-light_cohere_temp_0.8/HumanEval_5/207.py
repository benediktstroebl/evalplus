```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test the function with an empty list
test_empty() = intersperse([], 4)
# This should return an empty list
# test_empty() == []

# Test the function with a list of numbers
test_list = [1, 2, 3]
test_list = intersperse(test_list, 4)
# This should return [1, 4, 2, 4, 3]
# test_list == [1, 4, 2, 4, 3]

# Test the function with different delimiters
test_delimiters = [4, 3, 2, 1]
test_delimiters = intersperse(test_delimiters, 4)
# This should return [4, 3, 2, 1]
# test_delimiters == [4, 3, 2, 1]
```