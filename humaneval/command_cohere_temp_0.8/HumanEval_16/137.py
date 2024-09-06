Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to remove duplicate characters and converts the input string to lowercase to ensure that o, 0, and O are treated as the same character. It then returns the length of the resulting set which represents the number of distinct characters in the string.

To handle the tests, you can call this function with different input values and verify that the output matches the expected results:
```python
# Test case 1
input_string = 'xyzXYZ'
expected_result = 3
result = count_distinct_characters(input_string)
assert result == expected_result

# Test case 2
input_string = 'Jerry'
expected_result = 4
result = count_distinct_characters(input_string)
assert result == expected_result
```