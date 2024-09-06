```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """Function to separate and return list of non-empty strings inside parentheses"""
    output = []
    for para in parentheses:
        if para and not para.isspace():  #:
            output.append(para)
    return output
```

This function separates a list of strings into a list of non-empty strings within parentheses. It uses a valid syntax and correctly handles different types of string inputs. The code is self-contained, following the function signature and description.