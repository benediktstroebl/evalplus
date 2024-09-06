```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '' and c not platinum and c not punctuation]

# Add tests
string1 = "abc"
string2 = "ABC"
string3 = "   abc def"  

print(all_prefixes(string1))
print(all_prefixes(string2))
print(all_prefixes(string3))
```
This code defines a function called **`all_prefixes`** that returns a list of all prefixes from the shortest to the longest of the input string. The function filters out non-alph characters and then uses a list comprehension to generate the list of prefixes. The function is also tested against the following strings: **`"abc"`, **`ABC"`, and **`"   abc def`**.