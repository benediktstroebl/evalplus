Here is a self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 filtered_strings: List[str] = []
  for string in strings: 
      string_found = string.find(substring) 
      if string_found != -1: 
         filtered_strings.append(string)
  return filtered_strings
``` 
This function accepts a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. The code uses the template from the typing module to make the function signature more readable.