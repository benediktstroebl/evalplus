```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(). strings(string) for _ in range(1, len(string) + 1)]

# Test cases
string1 = 'ab'
string2 = 'abc'
string3 = 'abcabc'
string4 = ''
string5 = 'abc'

result1 = all_prefixes(string1)
print('Result for string1:', result1)

result2 = all_prefixes(string2)
print('Result for string2:', result2)

result3 = all_prefixes(string3)
print('Result for string3:', result3)

result4 = all_prefixes(string4)
print('Result for string4:', result4)

result5 = all_prefixes(string5)
print('Result for string5:', result5)
```
This script defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of the input string. It uses a Python list comprehension to iterate through the characters of the string and extract the prefixes. 

The test cases demonstrate how the function works with various input strings.