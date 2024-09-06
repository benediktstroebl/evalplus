```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.string() if p != '('] + ')'
    ```
This function uses a list comprehension to iterate over each character in the string, and if the character is not '(', then it adds it to the list of results. 

The function is designed to be easy to read and understand, and is self-contained, meaning that it does not rely on any other functions or variables.