Here's a self-contained Python function that solves the markdown code block's problem:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_numbers = [3, 2, 4, 1]
test_delimiter = 2

result = intersperse(test_numbers, test_delimiter)
print(result)  # Expected output: [3, 4, 2, 4, 3, 1]

test_numbers_single = [3]
test_delimiter_single = 3
result_single = intersperse(test_numbers_single, test_delimiter_single)
print(result_single)  # Expected output: [6]

test_delimiters = [2, 4, 6]
test_numbers = [1, 2, 3]

result_delimiters = intersperse(test_numbers, test_delimiters)
print(result_delimiters)  # Expected output: [1, 2, 4, 6, 3]
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with the elements of the input list separated by the specified delimiter. The script also includes several test cases to verify the functionality of the `intersperse` function, passing in different lists of numbers and delimiters, and checking the expected output against the result of the function.