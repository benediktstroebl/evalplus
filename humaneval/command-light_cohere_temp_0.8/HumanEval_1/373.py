```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """ Separate groups of nested parentheses into individual strings and return the list of those strings.

    :separate_paren_groups( [', ) ) 
    [', ')' 
    ['(', ')']

    :param parenthesis: list of strings containing parenthesis
    :return: list of strings, each being a separate group of parentheses
    """
    result = []
    for punctuation in parentheses:
        if not punctuation[0]:  # if no open parenthesis, add to result
            result.append(punctuation)
       
        elif punctuation[1] == '(':  # if open parenthesis, find closing parenthesis
            for close in result:
                if close[-1] == ')':
                    result.append(punctuation)
                    break
            else:
                result.append(close)
                break
        return result
```