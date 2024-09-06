```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate through each string in the input list and checks if the `substring` is present in each string. If the `substring` is found in a string, that string is included in the resulting list and returned. If the `substring` is not found in any of the strings, the function returns an empty list. 

This solution is concise and efficient, directly handling the filtering requirement specified in the problem statement. It can smoothly handle various scenarios, including both empty input lists and multiple occurrences of the substring within strings, owing to its elegant list comprehension approach.