```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
``` 
This code defines a function `filter_by_substring` that takes in a list of strings and a substring as arguments. The function creates a list comprehension that iterates over each string in the input list and checks if the string contains the given substring using the `contains` method.