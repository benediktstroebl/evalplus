```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called **`filter_by_substring`** that takes a list of strings and a substring as inputs. The function uses the string method **`contains`** to iterate through each string in the list, and if the substring is found in the string, it returns the string. The function then passes the string method **`contains`** to check if the substring is present in each string.