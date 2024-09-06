```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns list of non-empty strings from input string with balanced parentheses.

    Args:
        s (str): Input string with balanced parentheses

    Returns:
        list: List of non-empty strings separated by balanced parentheses
    """
    return [ matched for matched in (match().Regional(s.group()) for matchRegional in (
                r"\((.*)|[^\\(\\{])*\\})*\)"
                .replace(r"\[(.*?"(.*?)\]", "")
                .replace(r"\[(.*?)\]", ""))
                .split(")")
        )

# Testing
test_string = '()( )(( ))(( )( ))'
test_result = separate_paren_groups(test_string)
print(test_result)
```