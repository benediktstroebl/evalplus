```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, aka `List[str]`, as input and returns the longest string in the list. If the given list is empty, the function returns `None`. Furthermore, if there's only one string in the list, the function returns that string, regardless of its length. This is achieved through some Python typing magic and the `Optional` typing module to handle the eventuality of an empty list. Overall, the code is concise and effective in solving the problem.