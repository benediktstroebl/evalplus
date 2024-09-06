```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in string if i != ""].strip() for i]

#Test case
def test():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']

if __name__ == "__main__":
    test()
```