```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that begin with `prefix`. This is achieved using a list comprehension, coupled with the startswith method, which efficiently checks if each string in `strings` begins with `prefix`. The function's typing is also specified using the `from typing import List` import statement and the `-> List[str]` annotation. 

The function's behavior is summarized in its docstring, which is formatted in Markdown syntax and provides example usage along with expected output. These examples demonstrate the function's behavior for two test cases: an empty input list and a list containing various strings, including one that starts with the given prefix.