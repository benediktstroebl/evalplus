```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.join() for p in s.
    # New test string with an single open parenthesis is: (()
    # Find all closed parenthesis: () ... )
    # Find all open parenthesis: ( )
    # Replace all open parenthesis with a closed one
    # Return all strings between closed parenthesis
    return [')](p.join() for p in s.join() if p != '('))']
```
This code defines a function called `separate_paren_groups`, which takes a string `s` as input and returns a list of strings that can be separated from each other by balanced parentheses. 

It uses list comprehension and the `join()` function to replace all open parentheses with their corresponding closed version. 

Then it filters out any strings that contain only closed parenthesis.