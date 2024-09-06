```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')  # [abc, 'bacd', 'array']
 ``` 
This Python function uses the 'find' method to search for the substring in each string of the list. The function then returns a list of strings from the list that contain the given substring.