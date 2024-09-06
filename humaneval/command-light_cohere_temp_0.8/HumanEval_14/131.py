```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string) if char.isalpha()]

def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("xx") == []
    assert all_prefixes(" Luxiam Ward") == ['llux']
    assert all_prefixes("₎ La montee") == ['lo']
    assert all_prefixes(" CohereAI ") == ['ei']
test_all_prefixes()
```