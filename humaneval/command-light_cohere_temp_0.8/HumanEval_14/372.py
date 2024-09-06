```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha() orau"
    shortest prefix in string.
    return [] if string is "" 
    return ['a', 'ab', string[:1]] if string[0].isalpha() 
    return [string[1:]] if string[-1].isalpha()
    return [''.join(c) for c in string[1:-1] if c.isalpha()
   is the most common alpha characters in the string.
```