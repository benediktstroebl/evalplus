```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the substring."""
    return [x for x in strings if substring in x]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Expected output ['abc', 'bacd', 'array']
``` 
The code implements a function called **filter_by_substring** that takes two parameters: a list of strings **strings** and a substring **substring**. The function uses the **in** operator to filter the input list of strings and returns a new list that contains only the strings that contain the given substring.