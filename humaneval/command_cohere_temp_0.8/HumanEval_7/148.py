```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, containing only the strings from the input list that contain the given substring. It uses a list comprehension to iterate through each string in the input list and check if the substring is present in each string. If the substring is found, the string is included in the output list. If the substring is not found, the string is not included in the output list. 

This solution should pass the tests provided in the original problem statement. Let's verify it:
```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'arr'], 'a')
['abc', 'bacd', 'arr']
``` 

As expected, this solution passes all the test cases and correctly filters the input list of strings to contain only those strings that have the given substring. 

If you would like to test more scenarios or have further questions related to the function, feel free to ask.