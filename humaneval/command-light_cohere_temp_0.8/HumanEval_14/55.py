```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(). string(i) for i in range(len(string)) if string[i] != '']

# Sample input and expected output
input_str = 'abc'
print(all_prefixes(input_str))
# ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of an input string.  It uses a string and iterates through the length of the string, checking if each character is not an empty string. The output is a list of all prefixes found in the input string.