```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:1]] + ['abc', string[:2]] * (len(string) // 3)
for _ in range(10):
    string = ''.join() + random() * ('bc' if random() < 2 else 'a')
    print(all_prefixes(string))
``` 
Do you want me to help you with anything else related to code or with other technical topics?