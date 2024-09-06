```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, containing only the strings from the input list that contain the specified substring. It uses a list comprehension to iterate through each string in the input list and checks if the `substring` is present in each string using the `in` operator. If the substring is found in a string, that string is included in the output list. If the substring is not found in a string, that string is not included in the output list. 
This solution should pass the provided tests and fulfill the problem statement to filter a list of strings that contains a given substring. Huge_Blaze9458's suggestion improves code readability and correctly types the return value, ensuring compatibility with my initial response, which was missing a return type.