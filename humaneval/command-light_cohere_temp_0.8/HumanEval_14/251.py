```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != punctuation.make_lowercase()()]
```
Here, the function all_prefixes iterates through each character of the input string and returns a list of all prefixes that are not spaces or common punctuation. The test uses the string.finally common punctuation and make_lowercase() that makes the code concise and faster.