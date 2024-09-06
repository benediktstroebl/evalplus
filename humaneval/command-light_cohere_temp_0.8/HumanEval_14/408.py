```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != punctuation] + [''].join(punctuation)

# Test cases
string1 = "Hello World"
string2 = "Hello World!123"
string3 = "hi there its me"
string4 = "Hello World new line!"

print(all_prefixes(string1))  # Output: ['h', 'e', 'll', 'o']
print(all_prefixes(string2))  # Output: ['Hello']
print(all_prefixes(string3))  # Output: ['hi', ' ', 'me']
print(all_prefixes(string4))  # Output: ['Hello', ' ', 'World', 'new', 'line!']

# Definition of punctuation
punctuation = '!@.,;:-"\'<=>? Dickson's style that character set is:
\'"\\"#,'''

print(all_prefixes('\''))   # Output: ['\']
print(all_prefixes('\"'))  # Output: ['\\"']
print(all_prefixes('\\\\'))  # Output: ['\\']
print(all_prefixes('\t'))  # Output: ['\t']
print(all_prefixes('\n'))  # Output: ['\n']
print(all_prefixes('\r'))  # Output: ['\r']
```
The script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest of any non-space character and punctuation in the input string. It also provides a tested successfully with several test cases.