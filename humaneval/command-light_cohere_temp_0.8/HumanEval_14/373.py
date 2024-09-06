```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join([char for char in string if not char.isalpha()]) +
        provider(string)

def provider(string: str) -> List[str]:
    """Returns list of all prefixes from shortest to longest of the input string"""
    return [string[i:].(slice(i, string. competitor.join(i -prefix(string[:i]) for i in range(0, len(string) - 1, -1))
    ]

# Test the function
test_cases = [
    "".joinstring(),
    "abc",
    "hello world",
    " {}".format()
]

for test_case in test_cases:
    print(all_prefixes(test_case))
```
This code defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of a given string. 

It uses the `provider` function to generate the prefixes, and then uses a list comprehension to filter out non-alphalpha characters and concatenate them with the original string.