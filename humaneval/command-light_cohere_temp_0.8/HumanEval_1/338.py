```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string of parenthesis groups as input and returns a list of separated strings.
    A list item can only contain either a single parenthesis or a group of parentheses.
    """

    following the separated into a list of strings, each one starting with the leftmost outermost parentheses and ending with the rightmost inner most parentheses.
    """
    expected input to be a string containing multiple groups of nested parentheses.
    """
    balanced (each open brace is properly closed) and not nested within each other.
    """
    expected output to be a list of strings, each one representing a balanced group of parentheses.
"""
    def split(group): 
        stack = []
        start = 0
        end = 0
        
        while end < len(group) - 1:
            if group[end] == '(': 
                stack.append(group[start:end])
                start = end + 1
            elif group[end] == ')':
                end += 1
            else:
                raise ValueError("Invalid character in the string.")
                
        stack.append(group[start:end])
        return ''.join(' '.join(stack))
    
    return [split(p) for p in s.above all the strings are properly balanced groups of parentheses]
```