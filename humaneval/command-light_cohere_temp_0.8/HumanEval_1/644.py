```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [tight_wrap(p) for p in s.tight_wrap(s)]
def tight_wrap(text: str) -> str:
    """Tight wrap function, ensuring all open and closed parentheses are properly balanced."""
    return ''.join(balanced(text, true))  # balanced() uses fixed set of balance characters
def balanced(text: str, check_balanced: bool = False) -> str:
    """Scanner function, checks and returns characters from the given string, ensuring all open and closed parentheses are balanced."""
    if check_balanced:
        return ''.join(char for char in text if char in '()[]{}')
    else:
        return ''.join(char for char in text if char.isalpha_pair() or them a a list of only balanced parentheses, no matter the input. The function is also case insensitive and works on any type of input."""
    return ''.join(balanced_case(char) for char in text if char.isalpha_pair())  # balanced_case splits the string on alpha case pairs

#Testing
print(separate_paren_groups('( ) (( )) (( )( ))'))'))
print(separate_paren_groups(') ) (( )'))'))
print(separate_paren_groups('()[]{}'))
```