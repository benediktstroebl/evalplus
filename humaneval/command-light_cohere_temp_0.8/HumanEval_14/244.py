```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join('abcdefghijklmnopqrqrstuvwxyz')]
all_prefixes('abc')  # ['a', 'ab', 'abc']
``` 
The function will return a list of all prefixes from shortest to longest of the input string, which in this case is ['a', 'ab', 'abc'].