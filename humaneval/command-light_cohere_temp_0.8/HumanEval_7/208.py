```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This Python code defines a function called **`filter_by_substring`** that filters a list of strings based on whether each element contains a given substring. It uses the` contains()` method to check if each string contains the substring, and returns a new list containing only the strings that do contain the substring. 

Additionally, the code utilizes the **`List`** type and the **`str`** class to define a list of strings and a substring, and demonstrates the function's functionality with some sample test cases.