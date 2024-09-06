```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` which takes two parameters: `strings`, a list of strings, and `substring`, a single string. The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, paired with a generator expression, that filters elements based on the condition `substring in s`.

If given an empty list or an empty substring, this function would return an empty list as well. 
The given function is elegantly concise and functional-programming-like, making it readable and maintainable. 

This solution assumes Python 3, where list comprehensions and type annotations are both standard features.