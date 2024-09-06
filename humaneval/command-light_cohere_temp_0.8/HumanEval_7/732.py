```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
``` 
This code defines a Python function that takes in a list of strings and a substring as input, and returns a new list containing only the elements from the input list that contain the given substring. 

The `filter_by_substring` function utilizes a list comprehension to iterate over each element in the input list and check if the element contains the given substring using the `contains` method. 

This ensures that the function only adds elements to the output list if they contain the specified substring, effectively filtering the list based on the substring.