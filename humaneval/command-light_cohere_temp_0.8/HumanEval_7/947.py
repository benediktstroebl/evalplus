```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function called **`filter_by_substring`** that filters and returns a list of strings from a given input list **`strings`** that contain a specific substring **`substring`**. The function utilizes the **`contains`** method to check if each string contains the given substring. 

This approach efficiently filters out strings that do not contain the specified substring, making it a practical solution for many scenarios where you need to work with collections of strings.