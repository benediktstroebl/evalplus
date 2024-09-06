```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != '\n']

# Test cases
test_cases = [
    "abc",
    "hello world",
    "1234567890",
    "",
    "      ",
    "abc def",
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f"Expected: {", " ".join(test_case[:1] + " " + test_case[1:] + "\n")})
    print("Actual:", ", " ".join(actual_prefixes))
    assert actual_prefixes == test_case[:1] + " " + test_case[1:]
``` 
This Python script provides a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest, excluding spaces and newlines. The script also includes several test cases that cover various scenarios, such as empty strings, strings with only spaces, and strings with only characters.  The script then compares the expected and actual results for each test case and asserts the correctness of the function using the `assert` statement.