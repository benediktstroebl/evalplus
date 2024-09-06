```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in string if i != ""].lower() for i]

# Test cases
test_cases = [
    "abc",
    " Hello123 ",
    "  __with_quotes ",
    "",
    "abc123"
]

for text in test_cases:
    print(all_prefixes(text))
``` 
This function uses a list comprehension to filter all prefixes from the shortest to the longest, keeping only lowercase characters, which are considered prefixes in this context.