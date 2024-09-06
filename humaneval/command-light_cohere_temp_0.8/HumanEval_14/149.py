```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix in string and not prefix.isalpha(): break]
```

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('a') == ['a']
    assert all_prefixes('') == []
    assert all_prefixes('\n\ttest') == []
test_prefixes()
```