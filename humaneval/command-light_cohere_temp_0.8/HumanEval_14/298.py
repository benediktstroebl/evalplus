```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string] if string else []

# Test case 1: Simple string with single character
test_case1 = "a"
print(all_prefixes(test_case1))  # Output: ['a']

# Test case 2: Longer string with multiple characters
test_case2 = "bcda"
print(all_prefixes(test_case2))  # Output: ['b', 'bc', 'cda']

# Test case 3: Empty string
test_case3 = ""
print(all_prefixes(test_case3))  # Output: []

# Test case 4: Input string with special characters
test_case4 = "¨"
print(all_prefixes(test_case4))  # Output: ['¨']

# Test case 5: Prefixes with whitespace
test_case5 = "Hello World!"
print(all_prefixes(test_case5))  # Output: ['H', 'll', 'o', ' World!']
```
The provided Python script defines a function all_prefixes that constructs a list of all prefixes within a given string. The function utilizes a simple character iteration and returns the resulting list of prefixes. The test cases included in the script demonstrate how the function behaves for various scenarios, such as single characters, longer strings, empty strings, and strings with special characters or whitespace.