```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called **filter_by_substring** that takes two parameters: a list of strings **strings** and a substring **substring**. The function uses the **contains** method of the string class to check if each string in the input list contains the given substring.