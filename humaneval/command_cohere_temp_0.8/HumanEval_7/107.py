```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input and returns a new list containing only the strings from the input that contain the given substring. 

The code uses a list comprehension, creating a new list by iterating over each string in `strings` and checking if the `substring` is present in each string using the in operator. If the `substring` is found in the string, the string is included in the new list; otherwise, it is omitted. 

The typing annotation `List[str]` indicates that the function expects a list of string arguments and returns a list of strings.

This solution is efficient, taking linear time proportional to the number of strings in the list, as it checks each string only once to see if the substring exists. 

The solution is also concise, using a single line to iterate, filter, and return the new list, making it easy to understand and ready for production use. 

You can use assert statements to test this function:
```python
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ar') == ['array']
``` 
This will help ensure that the function behaves as expected.