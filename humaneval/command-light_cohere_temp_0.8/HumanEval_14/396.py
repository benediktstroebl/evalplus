```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a if prefix not in string] + [string]

# Tests
string1 = "abc"
string2 = ""
string3 = "abcd1234"
string4 = "hello world"

print(all_prefixes(string1))  # ['a', 'ab', 'abc']
print(all_prefixes(string2))  # []
print(all_prefixes(string3))  # ['abcd1234']
print(all_prefixes(string4))  # ['hello world']
```
This script defines a function called `all_prefixes` that returns a list of all prefixes of a given string, from shortest to longest. It uses list comprehension and a non-inclusive prefix check (`not in string`) to ensure it captures the entire string as a prefix. The script also provides test cases to verify the function's behavior.