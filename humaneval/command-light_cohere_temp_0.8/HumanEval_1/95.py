```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Separate each group of balanced parentheses from the input string into separate strings.

    : Open balanced parentheses with either single or double closing brace.

    : Returns the areas to separate groups with balanced parentheses:
    """
    result = []
    for para in parentheses:
        if para.count(')') > 0 and para.count('('):
            result.append(para.replace('()', ')))
        elif para.count(')') == 0 and para.count('('):
            result.append(para.replace(')', '')))
        else:
            result.append(para)
    return result
```
The purpose of this function is to split a string of parenthesis into individual groups. The function takes a list of strings as an argument, representing a string of parenthesis. It iterates through list of characters and checks if the current character is either '(' or ')', then it appends the character to the result string, and replace it with the corresponding closing character. If the character is not '(' or ')', then it appends the character to the result string, without any changes. 
The function returns the list of strings, which represent the individual groups of parenthesis in the original string.