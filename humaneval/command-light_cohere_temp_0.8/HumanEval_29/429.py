```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'
test_filter = [
    assert filter_by_prefix(strings, prefix) == ['abc', 'array'],
    assert not filter_by_prefix(strings, 'b')
    assert not filter_by_prefix([])
]
``` 
The provided code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function utilizes the `startswith` method to check if each string starts with the given prefix. The unit tests section ensures the validates the functionality of the `filter_by_prefix` function against different inputs and different strings.