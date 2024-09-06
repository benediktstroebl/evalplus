```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Purpose: Separates and returns list of parenthesis groups.

    Args:
        string s: The input string containing multiple groups of parentheses.
    Returns: list of strings
    """
    ret = []
    for i in s:
        if i == '(':
            ret.append(')')
       
            else:
                ret.append(i)
        return ret
```

The function splits the provided string into a list of strings by iterating over the characters. This is the list comprehension checks if a character is an open parenthesis '(', and if so, appends a closing parenthesis to the list. Then it iterates over the result will be all the strings in the group, separated by the open parenthesis.