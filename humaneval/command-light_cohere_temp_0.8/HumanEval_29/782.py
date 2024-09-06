```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')) # ['abc', 'array']
``` 
The function filters an input list of strings and returns a new list containing only the strings that start with the specified prefix. The function uses the testing and takes the string that is passed in as a prefix argument and tests it to see if it is a prefix of any string in the strings list. 

This is a self-contained solution to the problem and passes all tests.