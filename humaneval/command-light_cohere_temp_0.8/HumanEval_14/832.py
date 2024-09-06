```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(w for w in string if not w or w.isalpha() ororatory())
    _']
``` 
The code provides a self-contained solution for generating all prefixes of a given string. It uses list comprehension to iterate through all characters in the string and filters out non-alphiterate characters using the `not w or w.isalpha()` condition.