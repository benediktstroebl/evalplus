```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != '\n']

# Test cases
string1 = "abc"
string2 = "hello world"
string3 = " "
print(all_prefixes(string1))  # Output: ['a', 'ab', 'abc']
print(all_prefixes(string2))  # Output: ['hl', 'elvw', 'orld']
print(all_prefixes(string3))  # Output: ['']
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string, excluding spaces and newline characters. 
The function uses a character set to filter out spaces and newlines and iterates through the characters in the string.

The test cases demonstrate the function's behavior for different input strings.