```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate over each string in the input list and checks if the `substring` is present in each string. If the substring is found in a string, that string is included in the resulting list and returned. If the `substring` is empty or not provided, the function returns the entire input list unchanged. 

This solution should address the problem statement and correctly filter the input list according to the provided substring. Let me know if you'd like me to explain any part of the code in further detail. I'm also here to help if you have any additional questions or challenges related to the problem or any other topic in Python.