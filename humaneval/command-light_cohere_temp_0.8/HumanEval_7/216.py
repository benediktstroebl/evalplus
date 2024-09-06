```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This code defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The code utilizes the important list comprehension to iterate over each string and checks if the substring is present in the string using the `contains` method. 

This problem's well-contained and can be easily understood with the provided code.