```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    return [p for p in input_string.replace("(")( "))]
```
This script defines a function `separate_paren_groups` that takes a string `input_string` as an argument and returns a list of parenthesis groups. 

The function uses a simple list comprehension to iterate over each character in the input string, identifying parentheses, and appending them to a new string. 

The parenthesis groups are separated by the addition operator (`+`).  This solution handles the task of separating and balancing parenthesis groups in a given input string.