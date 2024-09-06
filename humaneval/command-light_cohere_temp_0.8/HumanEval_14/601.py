```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(w for w in string if not w or w.isalpha())]
print(all_prefixes('abc'))
```  This function returns a list of all prefixes from shortest to longest of the input string.