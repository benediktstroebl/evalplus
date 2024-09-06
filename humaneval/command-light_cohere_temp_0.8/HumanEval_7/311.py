```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
``` 
This Python code defines a function **`filter_by_substring`** that filters a list of strings for a given substring. 

It uses the **`List`** and **`str`** data types and the **`substring`** variable to filter the input list of strings. 
The output is a new list containing only the strings from the input list that contain the specified substring.