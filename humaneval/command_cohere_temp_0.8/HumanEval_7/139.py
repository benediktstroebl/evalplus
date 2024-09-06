```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate through each string in the input list and check if the `substring` is present in each string. If the `substring` is found in a string, that string is included in the resulting list and if the `substring` is not found, that string is not included in the resulting list.  The function returns the filtered list of strings. 

This solution should address the problem you had and should work correctly with both empty input lists and substrings, as well as providing the expected output for the example used in the markdown code block. Let me know if you have any more questions or if you would like me to address any other problems you may have!