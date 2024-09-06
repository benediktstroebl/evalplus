```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This Python code implements a function called **filter_by_prefix** that filters an input list of strings to remove those that do not start with a given prefix. It utilizes the ** typing module to handle the parameter types. This function works by iterating through each string in the list, and checking if it starts with the given prefix. If the check is successful, the string is added to a new list that will be returned. 

This code can be used to filter a list of strings for any given prefix.