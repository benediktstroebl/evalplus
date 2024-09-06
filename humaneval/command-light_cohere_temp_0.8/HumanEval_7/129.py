```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code implements a function called **filter_by_substring** that filters and returns a new list of strings from the input list **strings** that contain the given substring **substring**. 

The function uses the contains() method of strings. The contains() method returns True if the substring is found in the string, and False otherwise. 

The type of the function parameters is defined using the **typing** module, which allows us to specify the expected type of the function arguments and return values. 

The purpose of this function is to filter and return only the strings that contain the given substring, which is a common operation in text filtering and searching.