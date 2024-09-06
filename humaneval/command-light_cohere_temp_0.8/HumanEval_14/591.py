```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != '\n']

# Test cases
tests = [
    ("abc", ["a", "ab", "abc"])
    ("hello world", ["h", "el", "llo", "world"])
    ("abc123", ["a", "bc", "123"])
    ("9876543210abc", ["9876543210", "abc"])
    # add more test cases here

for string, expected in tests:
    print(all_prefixes(string), f"Expected: {expected}, Got: {string}")
``` 
This Python script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest of the input string.  The way to use this script is to define a string or list of strings, then call the `all_prefixes` function with that input, and print the output to compare it with the expected output.