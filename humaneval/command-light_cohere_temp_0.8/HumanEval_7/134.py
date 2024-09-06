```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring"""
    
    # Using a set ensures unique results
    return set(strings).filter(substring.filter(str.find(substring)))

    return []
``` 
This function takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the substring. It uses the filtering and the. will only return unique occurrences of the strings that contain the substring.