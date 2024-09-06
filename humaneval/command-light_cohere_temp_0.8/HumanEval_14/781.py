```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test cases
test_cases = [
    "abc",
    "abc123",
    "Hello World",
    " 1234",
    "