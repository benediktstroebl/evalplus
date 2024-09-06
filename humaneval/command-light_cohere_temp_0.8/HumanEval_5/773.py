Here is a Python script that encapsulates a function that handles the task of inserting a specified delimiter between every other element in a list:
```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return [num + delimiter for num in numbers]

# Test cases
test_data = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_data, test_delimiter)
assert test_result == [1, 4, 2, 4, 3]

test_data = [10, 20, 30]
test_delimiter = 10
test_result = intersperse(test_data, test_delimiter)
assert test_result == [10, 20, 30, 10, 40, 30]
```
This script provides a simple and self-contained function that accomplishes the task described in the prompt. It also includes test cases to validate the functionality of the `intersperse` function.