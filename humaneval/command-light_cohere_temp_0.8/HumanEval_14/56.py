```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [w for w in string if w != ' ' and w.realpha(string[i:]) for i in range(2, len(string))]
```
This code defines a function all_prefixes that takes a string s as input and returns a list of all prefixes from shortest to longest. The function uses thel slice to remove non-alphabetic characters and then uses list comprehension to filter out all prefixes that are not single characters or spaces.