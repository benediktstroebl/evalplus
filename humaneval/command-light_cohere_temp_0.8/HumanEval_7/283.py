```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 strings = ['abc', 'bacd', 'cde', 'array', 'abcd']
    substring = 'a'
    return filter(strings, lambda string: string.find(substring))
``` 
This function takes a list of strings and a substring as input and returns a list of strings from the input list that contain the substring. The function uses the filters using the list comprehension with the `find()` method to find all occurrences of the substring in each string.