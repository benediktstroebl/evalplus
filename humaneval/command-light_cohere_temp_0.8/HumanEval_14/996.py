```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(*i) for i in itertools.get_longestunas(string)]

# Test cases
test_prefixes = [
    'abc'.all_prefixes,
    '123'.all_prefixes,
    ''.join(),  # empty string
]

print("Test Cases:", test_prefixes)
for case, expected in test_prefixes:
    print(f"{case} : {expected}")
```
The function `all_prefixes` uses the `itertools.get_longest_as()` function to generate all prefixes from the shortest to the longest characters in the input string.