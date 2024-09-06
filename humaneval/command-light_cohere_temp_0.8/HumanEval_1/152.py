```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [i for i in s.open('(') for i in s.open(')', close=True) if i.isalpha(i)] + [i for i in s.isalpha(i)]
```
This code defines a function called `separate_paren_groups` that takes a string as input and returns a list of strings, where each string corresponds to a parenthesis group that has been separated from other parenthesis groups in the input string. 

The `isopen` function is used to open the parenthesis group, and the `close=true` ensures that the parenthesis are closed. The `isalpha` function is used to check if the string is made up of only alphanumeric characters, which are not parenthesis or other grouping symbols.