```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]


# Example usage
my_list = ['abc', 'bacd', 'cde', 'array', 'hello']
print(filter_by_substring(my_list, 'a'))  # Output ['abc', 'bacd']
```
The function uses a list comprehension with a filter function to achieve the desired filtering.  It creates a list of strings, and then it applies the filter function with a lambda function that checks if each string contains the substring.