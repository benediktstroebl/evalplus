```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
Here is a Python script that defines a function called **`filter_by_prefix`** which filters an input list of strings based on whether their prefix matches the given **`prefix`**. 

The function uses the Python List's **`startswith`** method to check if each string in the input list starts with the given prefix. 
Then, it returns a new list containing only the strings from the original list that start with the given prefix.