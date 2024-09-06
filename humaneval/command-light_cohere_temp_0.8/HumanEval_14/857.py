```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join + c for c in string if c != " " and c.
    return [] if len(string) == 0 else all_prefixes(string[1:]) + [string[0]]

def all_prefixes_test(test_str: str) -> None:
    assert all_prefixes("Hello") == ["elo"]
    assert all_prefixes("World") == ["dlro"]
    assert all_prefixes("!") == [""]
    assert all_prefixes("   ") == [""]
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("123") == ['1']
    assert all_prefixes("abcde") == ['abc', 'bcde']

# Run the function with some tests
all_prefixes_test("abc")
``` 
Do you want me to assist you with further code implementation or answer related questions?