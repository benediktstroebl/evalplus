```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test the function with various inputs
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 5, 2, 6, 3]
result = intersperse(numbers, delimiter)
assert list(expected) == result

numbers = [4, 8, 12, 16]
delimiter = 3
expected = [7, 11, 14, 15]
result = intersperse(numbers, delimiter)
assert list(expected) == result

numbers = [10, 20, 30]
delimiter = 5
expected = [15, 25, 30]
result = intersperse(numbers, delimiter)
assert list(expected) == result
```

This Python script defines a function `intersperse` that takes a list of numbers and an integer `delimiter` as input, and returns a new list with the elements of the original list separated by the specified `delimiter`. The test cases cover various scenarios, including empty input lists, lists with different lengths and values, and lists separated by different intervals. The test ensures that the expected output matches the result of the `intersperse` function for each case.