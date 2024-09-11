Here is a Python script that solves the given problem:

```markdown
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string and returns them as a list.

    :param paren_string: A string containing multiple groups of nested parentheses
    :return: A list of strings where each string is a separate group of parentheses
    """
    result = []
    open_brace = 0
    temp = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If we encounter an open parenthesis, increment the count and add the character to the temporary string
        if char == '(':
            open_brace += 1
            temp += char
        # If we encounter a close parenthesis
        elif char == ')':
            # If the current group is not empty (i.e., there's no close parenthesis without an open one right before)
            if open_brace > 0:
                # Decrement the count and add the character to the temporary string
                open_brace -= 1
                temp += char
            # If the current group is empty (i.e., we've encountered a close parenthesis without an open one right before)
            else:
                # If the result list is not empty and the last element in the result list is not a proper subset of the temporary string
                if result and not result[-1].startswith(temp + '(' * len(temp)):
                    # Add the temporary string to the result list
                    result.append(temp)
                # If the result list is empty or the last element in the result list is a proper subset of the temporary string
                else:
                    # Remove leading open parentheses from the temporary string
                    temp = temp.replace('(', '', 1)
                # Reset the temporary string
                temp = ''
        # If the current character is not a parenthesis
        else:
            # If the result list is not empty and the last element in the result list is not a proper subset of the temporary string
            if result and not result[-1].startswith(temp + '(' * len(temp)):
                # Add the temporary string to the result list
                result.append(temp)
            # If the result list is empty or the last element in the result list is a proper subset of the temporary string
            else:
                # Remove leading open parentheses from the temporary string
                temp = temp.replace('(', '', 1)
    
    # Add the last temporary string to the result list if it's not empty
    if temp:
        result.append(temp)
    
    # Add leading open parentheses to each string in the result list if the string is not empty
    for i in range(len(result)):
        if result[i]:
            result[i] = '(' * len(result[i]) + result[i]
    
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script uses a stack-like approach to keep track of the current group of parentheses. It iterates over each character in the input string, incrementing a count when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. When it encounters a space or a close parenthesis without a corresponding open parenthesis, it checks if the current group is a proper subset of the last element in the result list. If it is, it adds the current group to the result list. Finally, it adds leading open parentheses to each string in the result list.