I can help you with the implementation of the function that takes a string of parentheses and returns a list of separated groups:
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of those groups separated into individual strings.

    >>> separated_paren_groups(') ) (( )) (( )( ))')
    ['(', ')']
    [',()',')']
    """
    return [p for p in s.p.replace('\(', ')') for s.p in s.p.split('()')]
 x = []
        for i in range(0, len(s)-1):
            if s[i] == ')':
                x.append(s[i+1])
            else:
                x.append(s[i])
                if i == len(s)-1:
                    break
        return x
``` 
This function splits the string into a list of substrings, as described in the problem statement.