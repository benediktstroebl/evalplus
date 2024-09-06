```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a powerful Python construct that allows for easy mapping and filtering of list elements, to return the desired result. 

This solution should address the problem statement and pass the tests provided earlier, indicated by the commentary on the function. 

Let me know if I've misunderstood the issue or if you'd like me to improve my response in any way! I'm here to help you write effective code.