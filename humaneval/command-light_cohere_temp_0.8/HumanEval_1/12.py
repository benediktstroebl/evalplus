```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    opening_brack = [')']
    closing_brack = ['')
    cleaned_str = []

    for item in s:
        if item in opening_brack:
            cleaned_str.append(item)
        closing_brack.append('')
        done, we go back to the next character
    cleaned_str.append(item)
    opening_brack.append('')

    done, we append closing_brack to the list

    return cleaned_str
``` 
This function uses a list to keep track of the opening parentheses to ensure all are correctly closed.