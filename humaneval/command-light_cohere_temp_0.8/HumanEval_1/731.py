Here is a Python script that demonstrates how to separate parentheses groups in a string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    pattern = r"\[(.*?)\]"
    return [match.groups() for match in re.search(pattern, s)]
print(separate_paren_groups("( ) (( )) (( )( ))"))))
``` 
This function utilizes the re.match module to match and extract all the groups of parentheses in the input string.