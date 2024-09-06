Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count

# Tests
test_cases = [
    ('', 'a', 0),
    ('aaa', 'a', 3),
    ('aaaa', 'aa', 3)
]

for string, substring, expected in test_cases:
    asserted = how_many_times(string, substring)
    if asserted != expected:
        print(f"Test '{string}' '{substring}' failed. Expected {expected}, found {asserted}.")
    else:
        print(f"Test '{string}' '{substring}' passed.")
```

The function `how_many_times` takes two strings as input: `string` and `substring`. It counts the number of times the `substring` appears in the `string`, including overlapping instances. The function returns an integer representing the count of occurrences.

The test cases are designed to validate the function against different scenarios. For each test case, the expected count of occurrences is specified. The function is then called with the `string` and `substring`, and the actual count is compared with the expected count. If they don't match, an error message is printed, indicating that the test has failed. Otherwise, a passing message is displayed.

This solution provides a clear and efficient way to solve this problem and ensure it works across different scenarios. Feel free to ask any questions or further clarifications!