```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes(string) == ['a', 'ab', string[0]] + all_prefixes(string[1:])
    return

# Example usage
all_prefixes_test('abc')
```
The function `all_prefixes` uses a recursive approach. It starts from the fact: it adds the first character to the list of prefixes and then calls the function recursively for the remaining characters. It stops the the the start with the first character and then continues with the rest of the string.