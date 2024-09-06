```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This code defines a function called **`filter_by_substring`** that filters an input list of strings and returns a new list that contains only the elements that contain the given substring. 

The function utilizes the **`find()`** method from Python's string module to check if each element in the input string list contains the given substring. 

This approach is self-contained because it only involves the input parameters and does not rely on any external modules or functions.