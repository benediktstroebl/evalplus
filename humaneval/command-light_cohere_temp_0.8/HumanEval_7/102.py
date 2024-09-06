```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test case 1
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abcd", "cder", " hello"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abcd']

# Test case 3
strings = ["hello"]
sub = "be"
result = filter_by_substring(strings, sub)
print(result)  # Output: []
``` 
This script defines a function **filter_by_substring** that filters an input list of strings based on a given substring. It utilizes a relevant Python typing features and uses list comprehension to achieve the desired output. 

The provided test cases pass, so you can use this function for your markdown code block.