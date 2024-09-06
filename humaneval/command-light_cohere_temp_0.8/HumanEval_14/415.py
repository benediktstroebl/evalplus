```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [x for x in string[0::len:] if x.isalpha()]
 string. this is important the a lowest possible length prefix and we want to build the list from the shortest to the longest. We can use a simple slicing to achieve this and the list comprehension to filter the string accordingly.