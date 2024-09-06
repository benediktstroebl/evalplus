```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that filters an input list of strings based on whether their prefixes match the given **prefix**. The function uses the **startswith** method from Python strings to achieve this. The test returns a list containing the desired strings that match the given prefix. 

Please note that this code is self-contained and doesn't require any additional imports or external functions.