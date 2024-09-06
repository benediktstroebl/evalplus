Here is a self-contained Python script that solves the problem of separating different groups of parentheses from the given input string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.replace(')', '') for p in s.split('()')]
```

This script defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of strings created by splitting the input string into individual parentheses. The function uses the `replace` to remove the parentheses from each string and then uses the `split` method to split the string into individual characters.

The output of this function is a list of strings that have been separated from the given input string.