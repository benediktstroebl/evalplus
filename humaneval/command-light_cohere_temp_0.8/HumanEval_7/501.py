```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case with empty input list
test_filter_by_substring_empty()

# Test case with one string
test_filter_by_substring_one_string()

# Test case with one substring
test_filter_by_substring_one_substring()

# Test case with multiple strings and one substring
test_filter_by_substring_multiple_strings()
```
This Python script defines a function called **filter_by_substring** that takes two arguments: a list of strings and a substring. The function uses a string method **in** to check if each string in the list contains the given substring. 

You can use this script to test your code with different inputs and validate the results of the filter_by_substring function against the expected output.