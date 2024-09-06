```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input and returns a new list containing only the strings from the input that contain the given substring. 

The function utilizes list comprehension and a generator expression `(s for s in strings if substring in s)` to filter out only the strings that contain the given substring. 

Such list comprehension syntax is convenient for filtering or transforming multiple lists alike when utilizing Python's typing module, which the function does with the `from typing import List` statement. 

Would you like to make any further modifications or additions to this function? Feel free to suggest so, and I'll modify the script accordingly!