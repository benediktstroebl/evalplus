```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + [''].join(c for c in string if c.isalpha())

    def test_all_prefixes():
        string = "abc"
        assert all_prefixes(string) == ['a', 'ab', 'abc']

        string = "hello world 123"
        assert all_prefixes(string) == ['h', 'el', 'll', 'world', '123']

        string = ""
        assert all_prefixes(string) == []
``` 
Do you have anything else I can help you with?