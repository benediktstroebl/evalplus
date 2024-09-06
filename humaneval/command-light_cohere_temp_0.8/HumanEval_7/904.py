Here is a Python script that contains a self-contained function that filters an input list of strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The function uses the contains() method to check if each string in the list contains the given substring. The function then returns a list of all the strings that contain the substring. 

This function is self-contained as it only uses the input 'strings' and 'substring' parameters and provides an expected output. 

It efficiently filters the list in constant time using Python list methods, demonstrating a clean and concise solution for the given problem.