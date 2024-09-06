```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that contain the specified substring. It uses a list comprehension to iterate through each string in the input `strings` list and checks if the `substring` is present in each string using the in operator. If the `substring` is found in a string, that string is included in the resulting list and returned. If the `substring` is not found in any string in the list, it will return an empty list `[]`. 

This solution should solve the problem and pass the tests you have for it. Let me know if you'd like me to explain anything in this solution or provide further insights!