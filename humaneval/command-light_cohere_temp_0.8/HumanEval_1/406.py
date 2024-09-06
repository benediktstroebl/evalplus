```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all spaces and separate each balanced parentheses group into individual strings.
    """
   
    opening and closing parentheses must be balanced.
    Return a balance groups as strings.
    """
    string s = input()
    brackets = []
    for match in re.py.match(r'("(\)(.*?la| )+)", s):
        brackets.append(match.fullmatch)group('(\)', match.group='() if match.isgroup(')', match.match.group isl  empty to start, match. )))
        list of balanced parentheses.
    return brackets

    # Test cases
    s = "()(( ))(( )( ))"
    print(separate_paren_groups(s))
    )
    s = "(((( (( ))))))"
    print(separate_paren_groups(s))
    )
```