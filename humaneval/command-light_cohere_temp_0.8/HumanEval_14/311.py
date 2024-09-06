```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [s for s in string if s != '']

# Test cases
string1 = "abc"
string2 = ""
string3 = "___"
string4 = "abc abc"
string5 = "A"

print("Test case 1:", all_prefixes(string1))
print()
print("Test case 2:", all_prefixes(string2))
print()
print("Test case 3:", all_prefixes(string3))
print()
print("Test case 4:", all_prefixes(string4))
print()
print("Test case 5:", all_prefixes(string5))
```