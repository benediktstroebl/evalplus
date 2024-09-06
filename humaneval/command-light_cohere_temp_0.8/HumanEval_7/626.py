```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
The problem is efficiently solved with a Python script that employs the List comprehension and the `find()` method. The `find()` method is used to locate the occurrence of the given `substring` within each string in the `strings` list, and the resulting strings that contain the `substring` are returned. 
The script also uses the `List[str]` syntax to convert the original list of strings into a list of characters, which is more readable and concise.