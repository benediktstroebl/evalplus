```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function filters a list of strings and returns only the strings that start with the specified prefix. It uses the filter method with a generator expression to achieve this, and the list of strings is passed as the `strings` argument to the function.

This function is a good self-contained solution that can be used to solve the given problem, passing the test that it should pass on a list of strings and a prefix. It can be easily useful tool for working with strings and can be easily reused in various situations.