```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code defines a function called **`filter_by_substring`** that takes in a list of strings and a substring as arguments. The function returns a filtering the list of strings that contain the substring passed. 

The code demonstrates the function by passing the tests in the **input_tests** module.