```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + [""] * (len(string) - 2)

# Test cases
test_cases = [
    "abc",
    "abc123",
    "",
    "abc@",
    "123abc",
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f"Expected: {", ", ".join(test_prefixes_expected[i] for i,test_prefixes_expected in enumerate(test_case,1))})
    print(f"Actual: {", ", ".join(actual_prefixes))
    assert actual_prefixes == test_prefixes_expected
```
This code defines a function called `all_prefixes` that returns a list of all prefixes of a given string. The function uses a characters in the input string and filters out any non-alph characters, then adds an empty character to create the prefix and duplicates it to ensure the correct length of the output.

The `test_cases` list contains several test cases, and the code uses a loop to iterate over each test case. The actual function call is made with each test case, and the actual output is compared with the expected output. The code also uses the assert statement to check if the actual output is equal to the expected output.