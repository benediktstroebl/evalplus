```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `return_list`, which contains only the strings from the input list that contain the given substring. 

The function utilizes a list comprehension, which is a concise way to create lists in Python by applying a certain condition to each element of the existing list. In this case, the condition is that the string must contain the given substring. 

Such a list comprehension returns a new list that satisfies the provided condition. In case the given substring is not found in any of the input strings or the input list is empty, the function returns an empty list. 

This approach ensures a concise and efficient solution to the problem, easily adaptable to different scenarios. You can attach test cases to the function to ensure that it behaves as expected, forming a complete and robust solution to the problem.