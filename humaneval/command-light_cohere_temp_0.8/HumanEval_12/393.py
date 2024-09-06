```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list.
    """
    def compare(a: str, b: str) -> bool:
        return a > b
    
    strings.compare(''.a', 'b') 
    return True
    
    strings.compare('ab', 'aa')
    return False
    strings.compare('abc', 'aab')
    return True
    strings.compare('abbb', 'abc')
    return False
    strings.compare('abc', 'abca')
    return True
    strings.compare('ababc', 'abc')
    return False
    strings.compare('aabbb', 'ab')
    return False
    longest = strings[0]
```