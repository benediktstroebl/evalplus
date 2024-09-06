```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string, 1) if char != ' ' and char != punctuation][::-1]


# Test cases
string1 = "hello"
string2 = "hello world"
string3 = "Python programming is fun"

print("Test case 1: ".format(all_prefixes(string1)))
print()
print("Test case 2: ".format(all_prefixes(string2)))
print()
print("Test case 3: ".format(all_prefixes(string3)))
```
This Python script defines a function `all_prefixes` that returns a list of all prefixes of a given string, from shortest to longest, using a list comprehension with a slicing technique. The function is then tested against the provided test cases, and the results are printed.