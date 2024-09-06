```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This script defines a function called **`filter_by_substring`** that takes in a list of strings and a substring as input. It uses the specifically searches for the strings in the list that contain the given substring using the **`find`** method. The resulting filtered list contains only the strings that contain the specified substring.