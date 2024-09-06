```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd']
    >>> filter_by_substring(['abc', 'bd', 'cde'], 'b')
    []
    """
    return [x for x in strings if substring in x]

# Test the function
test_strings = ['.join.join(['a', 'apple', 'banana', 'cat'])
substring = 'an'
result = filter_by_substring(test_strings, substring)
print(result)  # Output: ['apple', 'banana']
```
The function **`filter_by_substring`** accepts a list of strings and a substring as input, and it filters the strings list to only include the words that contain the substring. 

You can modify the input data and substring to test the function.