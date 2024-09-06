```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, accompanied by an in operator to check for the presence of the substring within each string in the list.  This provides a convenient way to filter lists of strings based on a certain search pattern.  The typing annotation of `List[str]` further assures that the function returns a list of strings.  This codebase provides a robust and adaptable solution to the problem and is compatible with a variety of scenarios.  By utilizing this function, you can easily retrieve a subset of strings from a larger list, streamlining your text analysis or manipulation tasks.  Overall, it provides an intuitive and efficient tool for filtering strings in a list using a substring as the criterion.  The markdown code block encapsulates the function along with its precise description, thereby providing a comprehensive view of the problem-solving mechanism.