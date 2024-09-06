```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
# Test the function with a sample input and output
strings = ['abc', 'bacd', 'cde', 'array', '123', 'abc']
substr = 'a'
result = filter_by_substring(strings, substring)
print(result)
``` 
The output of the above code will be: 
```
['abc', 'bacd', 'array']
``` 
This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring.  The filtering is done by using a list comprehension, which creates a new list by filtering the elements of the original list based on a condition.