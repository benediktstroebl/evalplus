```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test case: Filter words starting with 'af'
test_filter_by_prefix = [
    "adaft", "aft", "adama", "afraid", "apple", "foraf", "afari"
].test_filter_by_prefix

result = filter_by_prefix(test_filter_by_prefix, 'af')
print(result)  # Output: ['adaft', 'afraid', 'apple']
``` 
The function `filter_by_prefix` takes a list of strings and a prefix as input and returns a new list of strings that start with the specified prefix.