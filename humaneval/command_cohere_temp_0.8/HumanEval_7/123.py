```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code snippet takes a list of strings `strings` and a substring `substring` as input, and returns a new list containing only the strings from the input that contain the given substring. This is accomplished using a list comprehension, creating a new list by applying a generator expression to the original list, filtering out strings that do not contain the given substring. 
```python
# Test Scenario
assert filter_by_substring([], 'a') == []

assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ar') == ['array']
```
This script can be tested against various test scenarios, including empty input lists, lists with different numbers of strings, and lists containing strings of different lengths, some of which include the substring and some of which do not. 
It's important to note that this function performs a case-sensitive search, meaning it will only match strings that contain the exact same case as the given substring. If you want to perform a case-insensitive search, you could modify the function to convert the input strings and substring to lowercase before performing the comparison. Furtheremore, This code uses Python's type hinting to indicate that the function takes a list of strings and a substring as input, and returns a new list of strings, which could be useful for static type checking and for improving the readability and maintainability of the code. 
Overall, the function is concise, efficient, and easy to use, making it a useful tool for solving this problem. Note that this code assumes that the input list is already sorted or is not sorted in a way that would affect the desired output. If the input list is unsorted and order matters, you may need to consider sorting the list before filtering.