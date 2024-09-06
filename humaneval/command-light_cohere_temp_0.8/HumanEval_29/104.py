```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'

print("Test case 1 result: ", end="")
print(filter_by_prefix(strings, prefix))
print("\n")

strings = ['a', 'b', 'abcd']
prefix = 'c'

print("Test case 2 result: ", end="")
print(filter_by_prefix(strings, prefix))
print("\n")

# Input case
input_strings = ["def", 'hello', "bye", "world"]
input_prefix = "def"

print("Input case result: ", end=")
print(filter_by_prefix(input_strings, input_prefix))
``` 
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filtered list of strings that start with the specified prefix. 

The script then has two test cases:
1. The first test case uses the empty list and the given prefix, which should return an empty list.
2. The second test case uses a list of strings with the specified prefix, and the output should be the list of strings starting with that prefix.

Finally, the script has an input case that uses an input list of strings and a specific prefix. The output should be the list of strings that start with the given prefix.