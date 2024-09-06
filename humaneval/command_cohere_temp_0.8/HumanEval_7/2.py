```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and checking if the `substring` is present in each string using the in operator. If the substring is found in a string, that string is included in the resulting list and, if not, it is excluded. 

This solution should address the problem statement and logic described, and correctly filter the input list according to the specified substring. Let me know if you would like to further clarify any technical details or discuss any other improvements or use cases related to the function. Please provide any additional information you may have to help guide our discussion and tailor it to your needs.