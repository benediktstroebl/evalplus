```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```

This Python script defines a function called longest in the above Markdown code block. The function takes a list of strings, `strings`, as input, and returns the longest string in the list. If the list contains multiple strings of the same length, it returns the first one. If the input list is empty, the function returns `None`. 

The function initially checks if the `strings` list is empty, and if so, it returns `None`. If the list is not empty, it checks if there is only one unique string length in the list. If there is only one unique string length, it returns any string from the list. If there are multiple distinct string lengths, it returns the string with the maximum length using the `max` function, specifying the custom `key` argument as `len` to determine the string length. 

This ensures that the function handles various scenarios and returns the longest non-empty string from the list while adhering to the problem's specific criteria.