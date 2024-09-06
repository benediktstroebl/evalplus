```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != '\n']

# Test cases
test_cases = [
    ("", ""),  # empty string
    "",          # empty character
    "abc",       # only one character
    "abc123",    # longer string
    " ABC123",    # case with capital letter at the beginning
    "a",         # has only one character
    "Hello, World!"  # has new line character
]

for test_str, expected_result in test_cases:
    actual_result = all_prefixes(test_str)
    assert actual_result == expected_result
 ```  This code defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest of the input string. The type of the string is inferred to be a string, and the function uses a list comprehension to iterate over every character in the string, and includes only those characters that are not spaces or new line characters. 
The test cases cover a variety of scenarios, including empty strings, single characters, longer strings, capital letters, and new line characters.  The test cases to verify that the function returns the expected result for different inputs.