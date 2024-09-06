```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two parameters: a list of strings (`strings`) and a substring (`substring`). The function returns a new list that includes only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension that iterates over each string in the input list and checks if the substring is a subset of that string, using the in operator. The resulting list of filtered strings is then returned as the output.  This solution is efficient and can quickly find the desired strings from the list containing the substring.