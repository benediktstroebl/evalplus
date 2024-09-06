```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This is accomplished using a list comprehension, filtering out elements that match the condition and returning the ones that start with the given prefix. 

This solution passes the provided test cases in the markdown block, as it correctly identifies strings that start with the given prefix. 

Let me know if you would like to provide additional test cases or discuss further how this solution works.